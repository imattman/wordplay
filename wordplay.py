#!/usr/bin/env python3

SCRABBLE_VALUES = {
    0: " -",
    1: "aeilnorstu",
    2: "dg",
    3: "bcmp",
    4: "fhvwy",
    5: "k",
    8: "jx",
    10: "qz",
}

letter_value = {
    letter: value
    for (value, letters) in SCRABBLE_VALUES.items()
    for letter in letters
}


def score_word(word):
    """Calculate the scrabble score for a string."""
    score = 0
    for letter in word:
        score += letter_value.get(letter, 0)
    return score


def load_lexicon_file(filepath):
    """Open and read lexicon word list from supplied file path."""
    with open(filepath) as fileobj:
        return read_words(fileobj)


def read_words(fileobj):
    """
    Read file-like object, tokenizing words on line boundaries.
    Blank lines and lines beginning with '#' are discarded.
    """
    words = []
    for line in fileobj:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        words.append(line.lower())

    return words


class Lexicon:

    def __init__(self, words):
        self._words = words
        self._scores = {w: (score_word(w), w) for w in words}

    def __len__(self):
        return len(self._words)

    def __iter__(self):
        return self._words.__iter__()

    def get_word(self, word):
        return self._scores.get(word, None)

    def __getitem__(self, word):
        return self.get_word(word)
