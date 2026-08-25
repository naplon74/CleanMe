<div align="center">

# CleanMe

<img src="https://github.com/naplon74/CleanMe/blob/main/data/icons/hicolor/scalable/apps/io.github.Naplon.CleanMe.svg" alt="CleanMe logo" width="180"/>

**Temporarily lock your keyboard and mouse so you can clean them safely.**

Minimal modern GNOME application for Linux.

![Version](https://img.shields.io/badge/version-0.1.1-yellow.svg)
![License](https://img.shields.io/badge/License-GPLv3-blue.svg)
![GTK](https://img.shields.io/badge/GTK-4-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux-orange.svg)

</div>

---

## Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/naplon74/CleanMe/blob/linux/data/screenshots/io.github.Naplon.CleanMe/1" width="45%" alt="Screenshot 1"/>
  <img src="https://raw.githubusercontent.com/naplon74/CleanMe/blob/linux/data/screenshots/io.github.Naplon.CleanMe/2" width="45%" alt="Screenshot 2"/>
</p>

> [!IMPORTANT]
> This is the **Linux** implementation of Clean Me.
>
> The Windows implementation is maintained separately in the [`windows`](../../tree/windows) branch.

## Features

* **Full input lock** - Blocks keyboard and mouse input.
* **Minimal fullscreen UI** - Native GTK 4 / GNOME interface.
* **Secure unlock** - Hold **Ctrl + Alt + U** for 3 seconds, in any order.
* **Accidental unlock protection** - Requires the key combination to be held continuously.
* **Custom background** - Use your own image.
* **Background blur** - Optional visual effect. This may impact performance.

## Installation

### Flatpak

A pre-built Flatpak package can be installed directly:

```bash
flatpak install CleanMe.flatpak
```

For development and building instructions, see the project files in this branch.

## Usage

Launch CleanMe and the application will temporarily lock keyboard and mouse input.

To unlock the application:

**Hold `Ctrl + Alt + U` for 3 seconds.**

The keys can be pressed in any order.

## Why Clean Me?

CleanMe is designed for a simple purpose:

* Clean your keyboard and mouse without triggering accidental keystrokes or clicks
* Temporarily lock input during cleaning
* Provide a lightweight native GNOME interface
* Keep the application focused on one task

## Development

The Linux version is a native GNOME application using **GTK 4**.

The Linux and Windows versions are maintained as independent codebases because they use different GUI frameworks, input handling and packaging systems.

## Windows

The Windows implementation uses Python and PyQt5.

→ [`windows` branch](../../tree/windows)

## License

Clean Me is released under the **GNU General Public License v3.0**.
