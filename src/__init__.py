def __init__(self, **kwargs):
    super().__init__(**kwargs)

    load_blur_css()

    self.settings = Gio.Settings.new("io.github.Naplon.CleanMe")

    self.alt_f4_enabled = self.settings.get_boolean("alt-f4-enabled")
    self.background_blur_enabled = self.settings.get_boolean("background-blur-enabled")

    background_path = self.settings.get_string("background-path")

    self.background_file = None
    if background_path:
        self.background_file = Gio.File.new_for_path(background_path)

    self.unlock_timer_id = None
    self.unlocking = False
    self.blurred_background_file = None
    self.blur_switch = None

    self.set_deletable(self.alt_f4_enabled)
    self.fullscreen()

    if self.background_file is not None:
        self.apply_background()

    key_controller = Gtk.EventControllerKey()
    key_controller.set_propagation_phase(Gtk.PropagationPhase.CAPTURE)
    key_controller.connect("key-pressed", self.on_key_pressed)
    key_controller.connect("key-released", self.on_key_released)
    self.add_controller(key_controller)

    self.connect("close-request", self.on_close_request)
