from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()

time.sleep(3)

while True:
    Keyboard.press(Key.f10)
    Keyboard.release(Key.f10)
    print('did it work?')
    time.sleep(12)
