# blur.py
#
# Copyright 2026 Naplon
#
# SPDX-License-Identifier: GPL-3.0-or-later

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk, Gdk


_BLUR_CSS = b"""
.blurred-background {
    filter: blur(20px);
}
"""


def load_blur_css() -> None:
    provider = Gtk.CssProvider()
    provider.load_from_data(_BLUR_CSS)

    display = Gdk.Display.get_default()

    if display is None:
        return

    Gtk.StyleContext.add_provider_for_display(
        display,
        provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
    )


def set_widget_blur(widget: Gtk.Widget, enabled: bool) -> None:
    if enabled:
        widget.add_css_class("blurred-background")
    else:
        widget.remove_css_class("blurred-background")
