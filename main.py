import sys
import threading
import time
import keyboard
import mouse
import os
import io
from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QImage
from settings import load_config


# Settings stuff, such a blur or image path or debuging (I use it for some test, it actually doesnt block the keyboard or anything)
settings = load_config()

blur = settings.get("blur", False)
debug = settings.get("debug", False)
image_path = settings.get("image_path", "")


# Special unlock combination
unlocked = False

combo_pressed = False
ctrl_held = False
alt_held = False
u_held = False
combo_hold_start = None


def block_all_keys(e):
    global combo_pressed, ctrl_held, alt_held, u_held, combo_hold_start

    if e.name == 'ctrl':
        ctrl_held = e.event_type == 'down'
    if e.name == 'alt':
        alt_held = e.event_type == 'down'
    if e.name == 'u':
        u_held = e.event_type == 'down'

    if ctrl_held and alt_held and u_held:
        if combo_hold_start is None:
            combo_hold_start = time.time()
        elif not combo_pressed and (time.time() - combo_hold_start >= 3):
            combo_pressed = True
        return True
    else:
        combo_hold_start = None

    return False


def block_mouse_move(e):
    mouse.move(0, 0, absolute=True, duration=0)
    return False


def block_mouse_click():
    return False


class LockScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Clean Me')
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setGeometry(
            0, 0,
            QApplication.primaryScreen().size().width(),
            QApplication.primaryScreen().size().height()
        )

        layout = QVBoxLayout()

        label = QLabel(
            'Clean Me is active.\nPress Ctrl+Alt+U for 3 seconds to unlock.\nSome settings can be modified using the yaml file.',
            self
        )
        label.setAlignment(Qt.AlignCenter)

        # readability improvement
        label.setStyleSheet("""
            font-size: 5em;
            color: white;
            background-color: rgba(0, 0, 0, 120);
            padding: 20px;
            border-radius: 10px;
        """)

        layout.addWidget(label)
        self.setLayout(layout)

        # -------------------------
        # BACKGROUND SYSTEM
        # -------------------------

        if image_path and os.path.exists(image_path):

            img = Image.open(image_path)
            img = img.resize(
                (self.width(), self.height())
            )

            if blur:
                img = img.filter(ImageFilter.GaussianBlur(radius=20))

            img = img.convert("RGB")

            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            qt_image = QImage.fromData(buffer.read())

            pixmap = QPixmap.fromImage(qt_image)

            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(pixmap))
            self.setPalette(palette)
            self.setAutoFillBackground(True)

        else:
            self.setStyleSheet("background-color: #222;")


    def keyPressEvent(self, event):
        pass

    def closeEvent(self, event):
        event.ignore()


def block_input():
    keyboard.hook(block_all_keys, suppress=True)
    mouse.hook(block_mouse_move)
    mouse.on_button(block_mouse_click, buttons=('left', 'right', 'middle'), types=('down', 'up'))


def unblock_input():
    global unlocked
    unlocked = True
    keyboard.unhook_all()
    mouse.unhook_all()


def listen_for_unlock(app):
    global unlocked, combo_pressed

    while not unlocked:
        if combo_pressed:
            unblock_input()
            app.quit()
            break
        time.sleep(0.1)


def main():
    app = QApplication(sys.argv)
    lock_screen = LockScreen()
    lock_screen.showFullScreen()

    # debug mode disables input blocking
    if not debug:
        threading.Thread(target=block_input, daemon=True).start()

    unlock_thread = threading.Thread(target=listen_for_unlock, args=(app,))
    unlock_thread.start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()