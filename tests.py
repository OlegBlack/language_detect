"""Documentation:
0.File name
1.Goal
2.Author
3.#ver / data creation/modification
4.License
"""

from constants import *
from utils import load_csv
from detect_language import detect_language

LANGUAGE_FREQ, ALLOWED_LETTERS, status = load_csv(CSV_FILE, CSV_SEP)

#Test itself
for expected_lang, sample_text in zip(['Finnish', 'Italian', 'Dutch', 'Czech'],
                                      [FINNISH_KIVI_TEXT,
                                       ITALIAN_BOCCACCIO_TEXT,
                                       DUTCH_ETHERLANDS_TEXT, CZECH_TEXT]):
    detected_language = detect_language(sample_text, LANGUAGE_FREQ, ALLOWED_LETTERS)
    # ground_truth vs predicted value
    # ground_truth - exppected_lang
    # predict value - predict value
    assert expected_lang == detected_language