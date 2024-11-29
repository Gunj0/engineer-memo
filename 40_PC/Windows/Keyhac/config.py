import sys
import os
import datetime

import pyauto
from keyhac import *

def configure(keymap):
    # 管理者権限で起動すること！！！
    # 他のアプリのショートカットが優先されることがあるため

    # 現在のキーマップを取得
    keymap_global = keymap.defineWindowKeymap()

    # 左Ctrlキーを仮想キー置き換え
    keymap.replaceKey( "LCtrl", 255 )

    # 仮想キーをホットキー化
    keymap.defineModifier( 255, "User0" )
    
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
    
    # カーソル+Alt
    keymap_global[ "U0-Alt-I" ] = keymap.InputKeyCommand("Alt-Up")
    keymap_global[ "U0-Alt-K" ] = keymap.InputKeyCommand("Alt-Down")
    keymap_global[ "U0-Alt-J" ] = keymap.InputKeyCommand("Alt-Left")
    keymap_global[ "U0-Alt-L" ] = keymap.InputKeyCommand("Alt-Right")
    
    # DELETE=Ctrl+Back
    keymap_global[ "U0-Back" ] = keymap.InputKeyCommand("Delete")
