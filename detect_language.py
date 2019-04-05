"""Documentation:
0.File name
1.Goal
2.Author
3.#ver / data creation/modification
4.License
"""

from utils import *

# get text frequencies
def detect_language(text, lang_freq, all_letters):
    """Calculate probabilities for supported languages of given text.
    @:param text - text to be analyzed, string.
    @:param lang_freq - pre-calculated frequencies for supported languages.
    @:param all_letters - list of letters taken in accounts.
    @:return detected language for given text as string."""
    # language for text
    predicted_language = '<undetected>'
    let_freq = calc_letter_frequency(text, all_letters)

    # MSE
    mse = calc_mse(lang_freq, let_freq)

    # Find out language itself as minimal value of MSE
    predicted_language = min(mse, key=mse.get)

    return predicted_language