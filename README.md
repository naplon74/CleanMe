<div align="center">
  <img src="assets/icon.png" alt="logo" width="250" />
<h3>Minimal modern Python app to temporarily lock your keyboard and mouse for cleaning. Unlock with a secure key combination. (Windows Only)</h3>

![Version](https://img.shields.io/badge/version-1.1-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

</div>

---

![Screenshot](assets/cleaner.png)

> [!IMPORTANT]
> This is the Windows version. Linux version can be found [here](https://github.com/naplon74/gnome-keyboard-cleaner).

## Installation
```
winget install Naplon_.KeyboardCleaner
```

## New
- Custom background image
- Background blur effect
- Debug mode (Usefull if you plan to touch the code)

## Features
- Locks all keyboard and mouse input.
- Minimal fullscreen GUI (PyQt5).
- Unlock by holding **Ctrl + Alt + U** for 3 seconds (in any order).
- Prevents accidental unlocks.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python main.py
   ```
3. To unlock, hold **Ctrl + Alt + U** for 3 seconds.

## Why?
- Clean your keyboard and mouse without accidental input.
- Lock input for focus or security.

