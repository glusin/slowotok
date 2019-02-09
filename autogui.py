import pyautogui

while True:
    position = str(pyautogui.position())
    print(position, flush=False, end='')
    print('\b' * len(position), flush=False, end='')



