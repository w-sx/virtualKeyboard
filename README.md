# Virtual Keyboard

**Simulates various keyboards, including numeric keyboards, extended function keyboards, and multimedia keyboards**

* Author: Shunxian Wu orchid.x@outlook.com
* Compatibility: NVDA 2022.1 or later

## Overview

This add-on provides multiple virtual keyboard modes, including numpad mode, function key extension mode, and multimedia keyboard mode. When the virtual keyboard is active, specific keys simulate other keys to offer extended functionality.

### Keys Involved

The keys involved in the virtual keyboard include:

* 7, 8, 9
* y, u, i, o, p, [, ]
* h, j, k, l, ;, '
* m, ,, ., /

Different virtual keyboard modes may utilize different keys. Use NVDA's input help mode to familiarize yourself with the virtual keyboard layout.

## Hotkeys

* **NVDA+Minus (NVDA+-):** Toggle the virtual keyboard on or off. Avoid modifying this gesture to prevent conflicts with virtual keyboard keys.
* **Left Bracket ([):** Switch to the previous mode when the virtual keyboard is open.
* **Right Bracket (]):** Switch to the next mode when the virtual keyboard is open.
* **Right Control (RightControl):** Pause or resume the virtual keyboard when it is open.

## Numpad Mode Key Mapping

When the virtual keyboard is enabled and switched to numpad mode, the key mappings are as follows:

* The keys 7, 8, 9 map to numpad 7, 8, 9
* The keys u, i, o map to numpad 4, 5, 6
* The keys j, k, l map to numpad 1, 2, 3
* The keys m, comma, period map to numpad 0, period, enter
* The keys y, p map to numpad slash, asterisk
* The keys h, semicolon map to numpad plus, minus
* The slash key maps to numpad Num Lock

### Recommended Fingering

To operate the virtual numpad area with one hand, place your right thumb on the m key, your index, middle, and ring fingers on the u, i, and o keys, respectively, and your little finger on the p key.

When the virtual keyboard is open, press the RightControl key at any time to pause or resume the virtual keyboard. Once paused, all keys except RightControl revert to their original 

## Function Key Extension Mode & Media Keys Mode

In these two modes, some uncommon function keys are mapped.

For specific key mappings, press NVDA+keyboard number 1 to open input help, switch to the corresponding mode, and click on the corresponding key to view.

## Changelog

2024.5

Merged numpad digits mode and numpad hotkey mode into numpad mode, switching with Num Lock

Added internationalization support

2024.4

Compatible with NVDA 2024.1

2023.3.27

Added Applied Media Keyboard, which can be used to implement functions such as next/previous song, volume up/down, and browser operations.

At the request of users, the mapping of the virtual keyboard enter key has been modified and added, corresponding to the comma key in numpad mode. The volume of the prompt for pausing/resuming the virtual keyboard has been increased.

Corrected errors in the help file, hopefully no other errors.