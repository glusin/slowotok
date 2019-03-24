from selenium import webdriver
from selenium.webdriver import ActionChains


class Browser:
    def __init__(self):
        self.driver = None
        self.int2char = dict()

    def open_slowotok(self):
        self.driver.get('http://www.slowotok.pl')

    def login(self, user, password):
        self.driver.find_element_by_id('login').click()
        user_input = self.driver.find_element_by_id('Email')
        password_input = self.driver.find_element_by_id('Password')
        user_input.send_keys(user)
        password_input.send_keys(password)
        for element in self.driver.find_elements_by_tag_name('input'):
            if 'Zaloguj mnie' in element.get_attribute('value'):
                element.click()
                break
        else:
            raise Exception('Nie znaleziono przycisku "Zaloguj mnie"')

    def start_game(self):
        for element in self.driver.find_elements_by_tag_name('a'):
            if 'Dołącz do gry' in element.text:
                element.click()
                break
        else:
            raise Exception('Nie znaleziono przycisku "Dołącz do gry"')

    def get_board(self):
        self.int2char = dict()
        for i in range(16):
            char = self.driver.find_element_by_id(str(i)).get_attribute('letter')
            self.int2char[i] = char

        return self.int2char

    def input_word(self, word):
        """słowo musi być zapisane jako lista numerów kafelków, które trzeba po kolei połaczyć"""
        action_chains = ActionChains(self.driver)
        start = self.driver.find_element_by_id(str(word[0]))
        action_chains.click_and_hold(start)

        for idx in word[1:-1]:
            target = self.driver.find_element_by_id(str(idx))
            action_chains.move_to_element(target)

        end = self.driver.find_element_by_id(str(word[-1]))
        action_chains.release(end).perform()

    def is_turn_beggining(self):
        time_left = self.driver.find_element_by_id('time').text
        minutes_left, seconds_left = time_left.split(':')
        if int(minutes_left) > 0 and int(seconds_left) > 30:
            return True
        else:
            return False


class Chrome(Browser):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome()


if __name__ == '__main__':
    chrome = Chrome()
    chrome.open_slowotok()
    chrome.login('o11142591@nwytg.net', 'R6Yez5yU7nPAczk')
    chrome.start_game()
    # chrome.input_word([2, 7, 6])
    print(chrome.is_turn_beggining())
