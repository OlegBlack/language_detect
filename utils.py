"""Documentation:
0.File name
1.Goal
2.Author
3.#ver / data creation/modification
4.License
"""

import pickle, os

from sklearn.metrics import mean_squared_error
from constants import *



def load_model():
    """load language frequencies from standard input .
        @:param **kwargs - dictionary with key "file_name" containing data model.
        @:return tuple (frequencies as dictionary, letters as list)"""
    # dictionary of supported languages
    lang_freq = {}
    # list of supported letters
    letters = []
    status = STATUS_SUCCES
    try:
        with open(PICKLE_FILE, "rb") as f:
            lang_freq = pickle.load(f)
            letters = pickle.load(f)
    except Exception as err:
        status = STATUS_FAIL

    return lang_freq, letters, status


# Sample text section
def load_csv(file=CSV_FILE, sep=','):
    """load language frequencies from standard input.
    @:param sep - separator for csv file, string.
    @:param file - csv file.
    @:return tuple (frequencies as dictionary, letters as list)"""
    status = STATUS_SUCCES
    # dictionary of supported languages
    lang_freq = {}
    # list of supported languages
    language_list = []
    # list of supported letters
    letters = []
    try:
        with open(file, encoding='utf-8') as let_file:
            # header
            header = let_file.readline().strip()
            items = header.split(sep)
            # items.pop(0)
            # language_list = items
            language_list = items[1:]

            # body
            for line in let_file.readlines():
                line = line.strip()
                if not line: continue
                items = line.split(sep)
                letter = items.pop(0)
                letters.append(letter)
                for lang, freq in zip(language_list, items):
                    freq = float(freq.split('%')[0]) / 100
                    if lang in lang_freq:
                        lang_freq[lang].update({letter: freq})
                    else:
                        lang_freq[lang] = {letter: freq}
    except Exception as err:
        print(err)
        status = STATUS_FAIL
    finally:
        if status == STATUS_SUCCES and not os.path.exists(PICKLE_FILE):
            with open(PICKLE_FILE, "wb") as f:
                pickle.dump(lang_freq, f)
                pickle.dump(letters, f)

    return lang_freq, letters, status


def calc_mse(lang_freq, let_freq):
    """Calculate Mean Square Error.
    @:param language_freq - pre-calculated frequencies for supported languages.
    @:param letters_freq - calculated frequencies for detected text.
    @:return dictionary of MSE for for supported languages."""
    # MSE dictionary for each language

    mse = {}
    for key, value in lang_freq.items():
        mse[key] = mean_squared_error([i for i in value.values()], list(let_freq.values()))
        # mse[key] = mse_l * 10000

    return mse


def calc_letter_frequency(text, all_letters):
    """Calculate frequencies for letters in detected text.
    @:param text - text to be analyzed, string.
    @:param all_letters - list of letters taken in accounts.
    @:return dictionary for calculated frequencies for detected text."""
    # total count of letters in text
    # letters_count = 0
    # dictionary for letter frequency in text

    letters_freq = {}

    if not all_letters:
        import string
        all_letters = string.ascii_lowercase
    text = text.lower()
    for ch in text:
        if ch not in all_letters: continue
        letters_freq[ch] = letters_freq.get(ch, 0) + 1
    letters_freq = {ch: letters_freq.get(ch, 0) / sum(letters_freq.values()) for ch in all_letters}

    return letters_freq
