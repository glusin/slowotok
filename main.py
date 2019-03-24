import time

import load
from Browser import Chrome

accepted_chars = set('weęrtyuioópaąsśdfghjklłzżźcćbnńm')  # litery występujące na planszy

words = load.get_polish_dict()
words = [slowo for odmiany_slowa in words for slowo in odmiany_slowa[:1]]
words = [w.lower() for w in words]
words = [w for w in words if set(w).issubset(accepted_chars)]
words = [w for w in words if 2 < len(w) < 14]  # słowa w grze mają dłogość [3, 13] liter
words = set(words)

combs = load.load_combinations('combinations.pkl')
combs = [c for c in combs if len(c) < 14]
combs = sorted(combs, key=lambda x: len(x), reverse=True)


def find_words(map_chars):
    int2char_ = dict()
    for i in range(16):
        int2char_[i] = map_chars[i]

    found_words = []
    found_combs = []
    n_found_words = 0
    for counter, c in enumerate(combs):
        word = ''.join([int2char_[int_] for int_ in c])
        if word in words:
            print(word, c)
            n_found_words += 1

            if word not in found_words:
                found_words.append(word)
                found_combs.append(c)

    return found_combs


if __name__ == '__main__':
    chrome = Chrome()
    chrome.open_slowotok()
    chrome.login('o11738634@nwytg.net', 'sfssp9ef9kiCArc')
    chrome.start_game()

    while True:
        print('Czekam na rozpoczęcie nowej tury')
        if not chrome.is_turn_beggining():
            time.sleep(1)
            continue
        int2char = chrome.get_board()
        letters = [int2char[i].lower() for i in range(16)]
        word_on_board = find_words(letters)
        for word in word_on_board:
            chrome.input_word(word)
