import pickle
import urllib.request
import zipfile

# prawdopodobnie potrzebujesz zaktualizować ten link - najłatwiej wyszukać poprzez "słownik odmian" w Google
POLISH_DICT_URL = r'https://sjp.pl/slownik/odmiany/sjp-odm-20190202.zip'


def to_sequence(structure):
    sequence = []
    for element in structure:
        if isinstance(element, str):
            sequence.append(element)
        else:
            sequence += to_sequence(element)

    return sequence


def get_polish_dict(dict_path='polski_slownik.zip'):
    try:
        z_f = zipfile.ZipFile(dict_path)
    except FileNotFoundError:
        urllib.request.urlretrieve(POLISH_DICT_URL, dict_path)
        z_f = zipfile.ZipFile(dict_path)
    data = z_f.open('odm.txt').read()
    data = data.decode('utf8')
    data = data.split('\r\n')
    data = [element.split(', ') for element in data]

    return data


def load_combinations(path):
    with open(path, 'rb') as pkl:
        combinations = pickle.load(pkl)
    return combinations
