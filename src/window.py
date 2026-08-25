# window.py
#
# Copyright 2026 Naplon
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os
import gi
import sys


gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw, Gdk, GLib, Gio
from PIL import Image, ImageFilter, ImageEnhance


def __init__(self, **kwargs):
    super().__init__(**kwargs)

    display = Gdk.Display.get_default()
    Gtk.Settings.get_for_display(display).set_property("gtk-icon-theme-name", "Adwaita")

    self.settings = Gio.Settings.new("io.github.Naplon.CleanMe")

BLURRED_BACKGROUND_PATH = os.path.join(
    GLib.get_tmp_dir(),
    "cleanme_blurred_background.png",
)


@Gtk.Template(resource_path="/io/github/Naplon/CleanMe/window.ui")
class CleanMeWindow(Adw.ApplicationWindow):
    __gtype_name__ = "CleanMeWindow"

    background_picture = Gtk.Template.Child()
    status_label = Gtk.Template.Child()
    debug_label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        self.settings = Gio.Settings.new("io.github.Naplon.CleanMe")

        self.unlock_timer_id = None
        self.unlocking = False

        self.alt_f4_enabled = self.settings.get_boolean("alt-f4-enabled")
        self.background_blur_enabled = self.settings.get_boolean("background-blur-enabled")
        self.background_file = None
        self.blurred_background_file = None
        self.blur_switch = None

        self.set_deletable(self.alt_f4_enabled)
        self.fullscreen()

        self.load_saved_background()

        key_controller = Gtk.EventControllerKey()
        key_controller.set_propagation_phase(Gtk.PropagationPhase.CAPTURE)
        key_controller.connect("key-pressed", self.on_key_pressed)
        key_controller.connect("key-released", self.on_key_released)
        self.add_controller(key_controller)

        self.connect("close-request", self.on_close_request)


    def load_saved_background(self):
        background_path = self.settings.get_string("background-path")

        if not background_path:
            return

        file = Gio.File.new_for_path(background_path)

        if not file.query_exists(None):
            self.settings.set_string("background-path", "")
            self.settings.set_boolean("background-blur-enabled", False)
            self.background_blur_enabled = False
            return

        self.background_file = file
        self.apply_background()

    def on_close_request(self, *args):
        return not self.alt_f4_enabled

    def on_key_pressed(self, controller, keyval, keycode, state):
        key_name = Gdk.keyval_name(keyval)

        ctrl_pressed = bool(state & Gdk.ModifierType.CONTROL_MASK)
        alt_pressed = bool(state & Gdk.ModifierType.ALT_MASK)

        if alt_pressed and key_name == "F4":
            if self.alt_f4_enabled:
                self.close()
            return True

        if ctrl_pressed and alt_pressed and key_name in ("s", "S"):
            self.open_settings()
            return True

        if ctrl_pressed and alt_pressed and key_name in ("u", "U"):
            if self.unlock_timer_id is None:
                self.unlocking = True
                self.status_label.set_label("Keep holding...")
                self.unlock_timer_id = GLib.timeout_add_seconds(3, self.unlock)

            return True

        return True

    def on_key_released(self, controller, keyval, keycode, state):
        key_name = Gdk.keyval_name(keyval)

        if key_name in ("u", "U", "Control_L", "Control_R", "Alt_L", "Alt_R"):
            self.cancel_unlock()

        return True

    def cancel_unlock(self):
        if self.unlock_timer_id is not None:
            GLib.source_remove(self.unlock_timer_id)
            self.unlock_timer_id = None

        if self.unlocking:
            self.unlocking = False
            self.status_label.set_label("Hold Ctrl + Alt + U for 3 seconds to unlock")

    def unlock(self):
        self.unlock_timer_id = None
        self.unlocking = False
        self.alt_f4_enabled = True
        self.close()
        return GLib.SOURCE_REMOVE

    def open_settings(self):
        dialog = Adw.PreferencesWindow(
            transient_for=self,
            modal=True,
            title="Clean Me Settings",
        )

        general_page = Adw.PreferencesPage(
            title="General",
            icon_name="preferences-system-symbolic",
        )

        keyboard_group = Adw.PreferencesGroup(title="Keyboard")

        alt_f4_row = Adw.ActionRow(
            title="Enable Alt + F4",
            subtitle="Allow Alt + F4 to close CleanMe",
        )

        alt_f4_switch = Gtk.Switch()
        alt_f4_switch.set_active(self.alt_f4_enabled)
        alt_f4_switch.set_valign(Gtk.Align.CENTER)
        alt_f4_switch.connect("notify::active", self.on_alt_f4_changed)

        alt_f4_row.add_suffix(alt_f4_switch)
        alt_f4_row.set_activatable_widget(alt_f4_switch)
        keyboard_group.add(alt_f4_row)

        background_group = Adw.PreferencesGroup(title="Background")

        choose_row = Adw.ActionRow(
            title="Choose background image",
            subtitle="Pick an image to display behind the lock screen",
        )

        choose_button = Gtk.Button(label="Choose")
        choose_button.set_valign(Gtk.Align.CENTER)
        choose_button.connect("clicked", self.choose_background)

        choose_row.add_suffix(choose_button)
        background_group.add(choose_row)

        blur_row = Adw.ActionRow(
            title="Blur background image",
            subtitle="Only available when a background image is selected",
        )

        self.blur_switch = Gtk.Switch()
        self.blur_switch.set_active(self.background_blur_enabled)
        self.blur_switch.set_sensitive(self.background_file is not None)
        self.blur_switch.set_valign(Gtk.Align.CENTER)
        self.blur_switch.connect("notify::active", self.on_blur_changed)

        blur_row.add_suffix(self.blur_switch)
        blur_row.set_activatable_widget(self.blur_switch)
        background_group.add(blur_row)

        general_page.add(keyboard_group)
        general_page.add(background_group)

        dialog.add(general_page)
        dialog.add(self.create_about_page())
        dialog.present()

    def create_about_page(self):
        about_page = Adw.PreferencesPage(
            title="About",
            icon_name="help-about-symbolic",
        )

        header_group = Adw.PreferencesGroup()

        about_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=12,
            margin_top=28,
            margin_bottom=28,
            margin_start=24,
            margin_end=24,
        )

        logo = Gtk.Image.new_from_icon_name("io.github.Naplon.CleanMe")
        logo.set_pixel_size(96)
        logo.set_halign(Gtk.Align.CENTER)

        name_label = Gtk.Label(label="Clean Me")
        name_label.add_css_class("title-1")
        name_label.set_halign(Gtk.Align.CENTER)

        description_label = Gtk.Label(
            label="A keyboard locking utility made for cleaning your keyboard without causing chaos."
        )
        description_label.add_css_class("dim-label")
        description_label.set_wrap(True)
        description_label.set_justify(Gtk.Justification.CENTER)
        description_label.set_halign(Gtk.Align.CENTER)

        about_box.append(logo)
        about_box.append(name_label)
        about_box.append(description_label)

        header_group.add(about_box)

        app_group = Adw.PreferencesGroup(title="Application")
        app_group.add(Adw.ActionRow(title="Version", subtitle="0.1.1"))
        app_group.add(Adw.ActionRow(title="Application ID", subtitle="io.github.Naplon.CleanMe"))
        app_group.add(Adw.ActionRow(title="Developer", subtitle="Naplon_"))

        license_group = Adw.PreferencesGroup(title="License")
        license_group.add(Adw.ActionRow(title="License", subtitle="GPL-3.0-or-later"))
        license_group.add(Adw.ActionRow(title="Copyright", subtitle="© 2026 Naplon"))

        shortcuts_group = Adw.PreferencesGroup(title="Shortcuts")
        shortcuts_group.add(Adw.ActionRow(title="Unlock", subtitle="Hold Ctrl + Alt + U for 3 seconds"))
        shortcuts_group.add(Adw.ActionRow(title="Open settings", subtitle="Ctrl + Alt + S"))
        shortcuts_group.add(Adw.ActionRow(title="Close with Alt + F4", subtitle="Optional, disabled by default"))

        about_page.add(header_group)
        about_page.add(app_group)
        about_page.add(license_group)
        about_page.add(shortcuts_group)

        return about_page

    def on_alt_f4_changed(self, switch, _):
        self.alt_f4_enabled = switch.get_active()
        self.set_deletable(self.alt_f4_enabled)
        self.settings.set_boolean("alt-f4-enabled", self.alt_f4_enabled)

    def choose_background(self, button):
        file_dialog = Gtk.FileDialog(title="Choose Background Image")

        image_filter = Gtk.FileFilter()
        image_filter.set_name("Images")
        image_filter.add_mime_type("image/png")
        image_filter.add_mime_type("image/jpeg")
        image_filter.add_mime_type("image/webp")
        image_filter.add_mime_type("image/bmp")

        filters = Gio.ListStore.new(Gtk.FileFilter)
        filters.append(image_filter)

        file_dialog.set_filters(filters)
        file_dialog.open(self, None, self.on_background_chosen)

    def on_background_chosen(self, dialog, result):
        try:
            file = dialog.open_finish(result)
        except Exception:
            return

        path = file.get_path()

        if path is None:
            return

        self.background_file = file
        self.blurred_background_file = None

        self.settings.set_string("background-path", path)

        if self.blur_switch is not None:
            self.blur_switch.set_sensitive(True)

        self.apply_background()

    def on_blur_changed(self, switch, _):
        if self.background_file is None:
            switch.set_active(False)
            self.background_blur_enabled = False
            self.settings.set_boolean("background-blur-enabled", False)
            return

        self.background_blur_enabled = switch.get_active()
        self.settings.set_boolean("background-blur-enabled", self.background_blur_enabled)
        self.apply_background()

    def apply_background(self):
        if self.background_file is None:
            self.background_picture.set_visible(False)
            return

        if self.background_blur_enabled:
            blurred_file = self.get_blurred_background_file()

            if blurred_file is not None:
                self.background_picture.set_file(blurred_file)
                self.background_picture.set_visible(True)
                return

        self.background_picture.set_file(self.background_file)
        self.background_picture.set_visible(True)

    def get_blurred_background_file(self):
        if self.blurred_background_file is not None:
            return self.blurred_background_file

        if self.background_file is None:
            return None

        path = self.background_file.get_path()

        if path is None:
            return None

        blurred_path = self.create_blurred_background(path)

        if blurred_path is None:
            return None

        self.blurred_background_file = Gio.File.new_for_path(blurred_path)
        return self.blurred_background_file

    def create_blurred_background(self, path):
        try:
            with Image.open(path) as image:
                image = image.convert("RGB")
                blurred = image.filter(ImageFilter.GaussianBlur(radius=24))
                blurred = ImageEnhance.Brightness(blurred).enhance(0.8)
                blurred.save(BLURRED_BACKGROUND_PATH, "PNG", optimize=True)

            return BLURRED_BACKGROUND_PATH

        except Exception as error:
            print(f"Could not blur background: {error}")
            return None
