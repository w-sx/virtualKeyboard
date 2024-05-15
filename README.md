# virtual keyboard

**Simulates various keyboards, including numeric keyboards, extended function keyboards, and multimedia keyboards**

* Author: Shunxian Wu orchid.x@outlook.com

* Compatibility: NVDA-2022.1 or later

## Overview

This plugin provides several virtual keyboard modes, including numpad mode, function key extension mode, and multimedia keyboard mode.

When the virtual keyboard is open and running, some keys will be simulated as other keys.

Keys that may be involved include:

* 7 8 9

* y u i o p [ ]

* h j k l ; '

* m , . /

Switching to different virtual keyboard modes may use different keyboard keys. You can use NVDA keyboard help to get familiar with the virtual keyboard layout.

## Hotkeys

* NVDA+- (minus sign), turn on/off the virtual keyboard. Do not modify the hotkey arbitrarily to avoid conflicts with virtual keyboard keys

* Left bracket [ , switch to the previous mode when the virtual keyboard is open

* Right bracket ], switch to the next mode when the virtual keyboard is open

* RightControl, pause or resume the virtual keyboard when the virtual keyboard is open

## Numpad Mode Key Mapping Table

Note: The following is the key mapping when the virtual keyboard is enabled and switched to numpad mode

* Keyboard 7, 8, 9 correspond to numpad 7, 8, 9

* Keyboard u, i, o correspond to numpad 4, 5, 6

* Keyboard j, k, l correspond to numpad 1, 2, 3

* Keyboard m, comma, period correspond to numpad 0, period, enter

* Keyboard y, p correspond to numpad slash, asterisk

* Keyboard h, semicolon correspond to numpad plus, minus

* Keyboard slash corresponds to numpad Num Lock

The recommended fingering is to place the right thumb on the m key, the index, middle, and ring fingers on the u, i, and o keys, and the little finger on the p key.

Using the above fingering, you can easily perform one-handed operations in the virtual numpad area.

When the virtual keyboard is open, you can press the RightControl key at any time to pause or resume the virtual keyboard. Once the virtual keyboard is paused, all keys except RightControl are restored to their original state.

## Function Key Extension Mode & Applied Media Extension Mode

In these two modes, some uncommon function keys are mapped.

This is for setting up simple and quick hotkeys for easy use in setting up single-key hotkeys or hotkeys that can be executed with just NVDA modifiers in input and gestures.

For specific key mappings, press NVDA+keyboard number 1 to open input help, switch to the corresponding mode, and click on the corresponding key to view.

## Additional Tips

When change the hotkey to turn on/off the virtual keyboard, please avoid the keys involved in the virtual keyboard.

Specifically, this includes:

7, 8, 9

y, u, i, o, p, left bracket, right bracket

h, j, k, l, semicolon, single quote

n, m, comma, period, slash

If you must set a hotkey related to the above keys, you can press RightControl before turning off the virtual keyboard.

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