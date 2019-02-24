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
    for char in word:
        score += letter_value.get(char, 0)
    return score
