from pynput import keyboard
import sys
from lohe import TIME

def on_press(key):
    if str(key) == 'Key.esc':
        sys.exit()
    else:
        print(TIME().Years() + ' | ' + TIME().Hors() +  f': {key}')

with keyboard.Listener(
    on_press = on_press) as listener:
    listener.join()
    