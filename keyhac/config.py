import sys
import os
import datetime

import pyauto
from keyhac import *


def configure(keymap):

    keymap_global = keymap.defineWindowKeymap()

    # 右Ctrl(CapsLock)を置き換え
    keymap.replaceKey( "LCtrl", 255 )

    # ホットキー化
    keymap.defineModifier( 255, "User0" )

    # USER0-Up/Down/Left/Right
    keymap_global["U0-I"] = "Up"
    keymap_global["U0-J"] = "Left"
    keymap_global["U0-K"] = "Down"
    keymap_global["U0-L"] = "Right"

    # USER0-Shift-Up/Down/Left/Right
    keymap_global["U0-Shift-I"] = "Shift-Up"
    keymap_global["U0-Shift-J"] = "Shift-Left"
    keymap_global["U0-Shift-K"] = "Shift-Down"
    keymap_global["U0-Shift-L"] = "Shift-Right"

    # USER0-Win-Up/Down/Left/Right
    keymap_global["U0-Win-I"] = "Win-Up"
    keymap_global["U0-Win-J"] = "Win-Left"
    keymap_global["U0-Win-K"] = "Win-Down"
    keymap_global["U0-Win-L"] = "Win-Right"
