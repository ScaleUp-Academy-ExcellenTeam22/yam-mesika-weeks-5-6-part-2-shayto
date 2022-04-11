import time
from typing import Iterable


def build_words_list(file_name: str) -> list:
    """
    :param file_name: from where we are to read words.
    :return: List with all words as values.
    """
    with open(file_name, 'r') as fdr:
        return fdr.read().split()


def find_word(iterable: Iterable, word: str) -> bool:
    """
    :param iterable: Data structure to make search.
    :param word: A word to find.
    :return: True if the word exist else False.
    """
    return word in iterable


def sum_how_long_to_search(iterable: Iterable) -> float:
    """
    :param iterable: search using iteration
    :return: How much time it took to make one search.
    """
    start_time = time.time()
    find_word(iterable, "zwitterion")
    end_time = time.time()
    return end_time - start_time


def average_runtime(iterable: Iterable) -> float:
    """
    :param iterable: search using iteration
    :return: The average amount of time it took to make 1000 searches.
    """
    count = 0
    for _ in range(1000):
        count += sum_how_long_to_search(iterable)
    return count / 1000


if __name__ == '__main__':
    words_list = build_words_list("words.txt")
    words_set = set(words_list)

    print(average_runtime(words_list))
    print(average_runtime(words_set))
