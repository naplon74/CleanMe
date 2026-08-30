<div align="center">

# Clean Me

<img src="https://raw.githubusercontent.com/naplon74/CleanMe/bed3767fd69c8533e595055c9c8bf69d4001fe82/data/icons/hicolor/scalable/apps/io.github.Naplon.CleanMe.svg" alt="Keyboard Cleaner logo" width="220" />

**Temporarily lock your keyboard and mouse so you can clean them safely.**

A lightweight keyboard and mouse cleaning utility for **Windows and Linux**.

</div>

---

## Platforms

Keyboard Cleaner has two independent implementations.

They are maintained in separate Git branches because the applications use different technologies and have different codebases.

| Platform | Branch                          | Technology             |
| -------- | ------------------------------- | ---------------------- |
| Windows  | [`windows`](../../tree/windows) | Python + PyQt5         |
| Linux    | [`linux`](../../tree/linux)     | Python + GTK 4 / GNOME |

### Windows

The Windows version is a minimal PyQt5 application designed specifically for Windows.

→ [`windows` branch](../../tree/windows)

### Linux

The Linux version is a native GNOME application built with GTK 4.

→ [`linux` branch](../../tree/linux)


---

## Features

Both versions provide the same core purpose:

* Temporarily lock keyboard and mouse input
* Fullscreen cleaning interface
* Secure unlock mechanism
* Protection against accidental unlocking
* Custom background support
* Background blur effects

Individual features may differ between platforms.

---

## Development

Clone the repository and switch to the branch for the platform you want to work on:

```bash
git clone https://github.com/naplon74/CleanMe.git
cd CleanMe
```

### Windows

```bash
git switch windows
```

See the [`windows` branch](../../tree/windows) for installation and development instructions.

### Linux

```bash
git switch linux
```

See the [`linux` branch](../../tree/linux) for installation and development instructions.

---

## License

Both Windows and Linux version are licensed under the GNU General Public License v3.0 license.
