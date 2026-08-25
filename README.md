<div align="center">
  <img src="https://raw.githubusercontent.com/naplon74/CleanMe/bed3767fd69c8533e595055c9c8bf69d4001fe82/data/icons/hicolor/scalable/apps/io.github.Naplon.CleanMe.svg" alt="Keyboard Cleaner logo" width="250" />

<h3>Minimal modern Python app to temporarily lock your keyboard and mouse for cleaning. Unlock with a secure key combination.</h3>

![Version](https://img.shields.io/badge/version-1.1-blue.svg)
![License](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)

</div>

---

<img src="https://raw.githubusercontent.com/naplon74/CleanMe/refs/heads/main/assets/cleaner.png">

> [!IMPORTANT]
> This is the **Windows** implementation of Keyboard Cleaner.
>
> The Linux implementation is maintained separately in the [`linux`](../../tree/linux) branch.

## Installation

The easiest way to install Keyboard Cleaner is with WinGet:

```powershell
winget install Naplon_.KeyboardCleaner
```

(might be broken)

## Features

* **Full input lock** - Locks keyboard and mouse input.
* **Minimal fullscreen GUI** - Built with PyQt5.
* **Secure unlock** - Hold **Ctrl + Alt + U** for 3 seconds, in any order.
* **Accidental unlock protection** - Requires the key combination to be held continuously.
* **Custom background** - Use your own background image.
* **Background blur** - Apply a blur effect to the background.
* **Debug mode** - Useful when developing or modifying the application.

## Usage

After installation, launch Keyboard Cleaner.

To unlock the application:

**Hold `Ctrl + Alt + U` for 3 seconds.**

The keys can be pressed in any order.

## Development

### Requirements

* Windows
* Python
* PyQt5

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

### Debug mode

Debug mode can be used when developing or modifying the application.

It can help diagnose issues without having to package the application first.

## Why?

Keyboard Cleaner is designed for a simple purpose:

* Clean your keyboard and mouse without accidental input
* Prevent unwanted clicks and keystrokes
* Temporarily lock input during cleaning or focus sessions

## Linux

The Linux implementation is a separate GNOME application.

→ [`linux` branch](../../tree/linux)

## License

Keyboard Cleaner for Windows is released under the **MIT License**.
