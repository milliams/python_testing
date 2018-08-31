"""
A miscelansous collection of functions which are useful for demonstrating testing
"""

from collections import Counter
import string

import requests


def add_elements(a, b):
    """
    Given two lists, add them together elementwise and return the result

    Examples:
        >>> add_elements([1, 2], [3, 4])
        [4, 6]
    """
    z = []
    for i in range(len(a)):
        z.append(a[i] + b[i])
    return z


def get_gutenberg_text(book: str) -> str:
    """
    Given a string of a Project Gutenberg book, return only the actual book content.
    """
    in_book = False
    result = []
    for line in book.split('\n'):
        if line.startswith('*** END OF THIS PROJECT GUTENBERG EBOOK'):
            break
        if in_book:
            result.append(line)
        if line.startswith('*** START OF THIS PROJECT GUTENBERG EBOOK'):
            in_book = True
    return '\n'.join(result)


def word_count(text: str, word: str='') -> int:
    """
    Count the number of occurences of ``word`` in a string.

    If ``word`` is not set, count all words.
    """
    if word:
        count = 0
        for text_word in text.split():
            if text_word == word:
                count += 1
        return count
    else:
        return len(text.split())


def count_capital_words_in_website(url: str) -> int:
    """
    Given a URL, count the number of words which start with a capital letter
    """
    text = requests.get(url).text
    count = 0
    for text_word in text.split():
        if text_word[0] in string.ascii_uppercase:
            count += 1
    return count
