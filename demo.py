""" -*- coding: utf-8 -*-
#
# Sample program for language detection
# Link to original paper https://www.kleemans.ch/letter-frequency
#
# How to run
# 1. add environment PYTHONIOENCODING="UTF-8"
# 2. python language_detect.py < letter_frequency.csv
#
"""

import os

from constants import *
from utils import load_csv, load_model
from detect_language import detect_language


# Demo app
if __name__ == "__main__":
    # # Load pre-calculated values
    language_freq, allowed_letters, status = load_model()
    print(status)
    if status != STATUS_SUCCES:
        language_freq, allowed_letters, status = load_csv(sep=CSV_SEP)
    # print(status)
    if status != STATUS_SUCCES:
        csv_file = input(PROMPT) # Ask user for file
        language_freq, allowed_letters, status = load_csv(file=csv_file, sep=CSV_SEP)
    if status != STATUS_SUCCES:
        os._exit(STATUS_EXIT)

    # For each sample text detect its language
    for expected_lang, sample_text in zip(['Finnish', 'Italian', 'Dutch', 'Czech'],
                                          [FINNISH_KIVI_TEXT,
                                           ITALIAN_BOCCACCIO_TEXT,
                                           DUTCH_ETHERLANDS_TEXT, CZECH_TEXT]):
        detected_language = detect_language(sample_text, language_freq, allowed_letters)
        print('Expected / detected language: {} / {}'.format(expected_lang, detected_language))
