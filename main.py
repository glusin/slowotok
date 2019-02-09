import time

import pyautogui

import load

# o11142591@nwytg.net
# R6Yez5yU7nPAczk

accepted_chars = set('weęrtyuioópaąsśdfghjklłzżźcćbnńm')

words = load.get_polish_dict('polish.txt')
words = [slowo for odmiany_slowa in words for slowo in odmiany_slowa[:1]]
words = [w.lower() for w in words]
words = [w for w in words if set(w).issubset(accepted_chars)]
words = [w for w in words if 2 < len(w) < 14]
words = set(words)

combs = load.load_combinations('combinations.pkl')
combs = [c for c in combs if len(c) < 14]
combs = sorted(combs, key=lambda x: len(x), reverse=True)


start_time = time.time()
int2char = dict()
for i in range(16):
    int2char[i] = 'ikloynornctyzyźs'[i]

found_words = []
found_combs = []
n_found_words = 0
for counter, c in enumerate(combs):
    word = ''.join([int2char[int_] for int_ in c])
    if word in words:
        print(word, c)
        n_found_words += 1

        if word not in found_words:
            found_words.append(word)
            found_combs.append(c)


start = (638, 198)
dx = dy = 120
pyautogui.PAUSE = 0.05
for combination in found_combs:
    for counter, block in enumerate(combination):
        x = block % 4
        y = block // 4
        to_x = start[0] + dx*x
        to_y = start[1] + dy*y
        pyautogui.dragTo(x=to_x, y=to_y, mouseDownUp=False)
        if counter == 0:
            pyautogui.mouseDown(x=to_x, y=to_y)

    pyautogui.mouseUp()
    if time.time() - start_time > 80:
        break
