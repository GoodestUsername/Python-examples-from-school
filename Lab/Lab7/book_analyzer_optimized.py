"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""
import functools
import time
from collections import defaultdict


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = ",*;.:([])"

    def __init__(self):
        self.text = None

    @functools.lru_cache(maxsize=128)
    def remove_common_punctuation(self, word):
        """
        Returns word without common punctuations.
        :param word: A string.
        :return: A string without common punctuations.
        """
        for punctuation in self.COMMON_PUNCTUATION:
            word = word.replace(punctuation, '')
        return word

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()

        # convert list of lines to dict of words that have punctuation removed, and ignores blank lines
        word_freq = defaultdict(int)
        for line in self.text:
            if line != "\n":  # run if not just new line
                for word in line.split():
                    word = self.remove_common_punctuation(word)
                    word_freq[word.lower()] += 1
        self.text = word_freq

    def find_unique_words(self):
        """
        Filters out all the words in the text.
        :return: a list of all the unique words.
        """
        return self.text.keys()


def main():
    start_time = time.time()
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    for word in unique_words:
        print(word)
    print("-" * 50)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
