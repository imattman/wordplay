#!/usr/bin/env python3

SCRABBLE_VALUES = {
    0:  " -",
    1:  "aeilnorstu",
    2:  "dg",
    3:  "bcmp",
    4:  "fhvwy",
    5:  "k",
    8:  "jx",
    10: "qz",
}

letter_value = {}
for (value, letters) in SCRABBLE_VALUES.items():
    for letter in letters:
        letter_value[letter] = value


def score_word(word):
    score = 0
    for letter in word:
        score += letter_value.get(letter, 0)
    return score


def load_lexicon_file(filepath):
    with open(filepath) as fileobj:
        return read_words(fileobj)


def read_words(fileobj):
    # this felt a little too involved for a single comprehension
    words = []
    for line in fileobj:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        words.append(line.lower())

    return words
