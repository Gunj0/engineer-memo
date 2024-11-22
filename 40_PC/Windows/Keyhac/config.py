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


# 以下は弥生PC用
    # 左ctrlキーをモディファイアキー(U0)に登録
    keymap.replaceKey("RAlt", 255)
    keymap.defineModifier(255, "User0")

    keymap_global = keymap.defineWindowKeymap()
    
    # カーソル
    keymap_global[ "U0-I" ] = keymap.InputKeyCommand("Up")
    keymap_global[ "U0-K" ] = keymap.InputKeyCommand("Down")
    keymap_global[ "U0-J" ] = keymap.InputKeyCommand("Left")
    keymap_global[ "U0-L" ] = keymap.InputKeyCommand("Right")

    # カーソル+Shift
    keymap_global[ "U0-S-I" ] = keymap.InputKeyCommand("S-Up")
    keymap_global[ "U0-S-K" ] = keymap.InputKeyCommand("S-Down")
    keymap_global[ "U0-S-J" ] = keymap.InputKeyCommand("S-Left")
    keymap_global[ "U0-S-L" ] = keymap.InputKeyCommand("S-Right")

    # カーソル+Ctrl
    keymap_global[ "U0-C-I" ] = keymap.InputKeyCommand("C-Up")
    keymap_global[ "U0-C-K" ] = keymap.InputKeyCommand("C-Down")
    keymap_global[ "U0-C-J" ] = keymap.InputKeyCommand("C-Left")
    keymap_global[ "U0-C-L" ] = keymap.InputKeyCommand("C-Right")

    # カーソル+Ctrl+Shift
    keymap_global[ "U0-S-C-I" ] = keymap.InputKeyCommand("S-C-Up")
    keymap_global[ "U0-S-C-K" ] = keymap.InputKeyCommand("S-C-Down")
    keymap_global[ "U0-S-C-J" ] = keymap.InputKeyCommand("S-C-Left")
    keymap_global[ "U0-S-C-L" ] = keymap.InputKeyCommand("S-C-Right")

    # カーソル+Win
    keymap_global[ "U0-LWin-I" ] = keymap.InputKeyCommand("LWin-Up")
    keymap_global[ "U0-LWin-K" ] = keymap.InputKeyCommand("LWin-Down")
    keymap_global[ "U0-LWin-J" ] = keymap.InputKeyCommand("LWin-Left")
    keymap_global[ "U0-LWin-L" ] = keymap.InputKeyCommand("LWin-Right")
    
    # DELETE=Ctrl+Back
    keymap_global[ "U0-Back" ] = keymap.InputKeyCommand("Delete")
