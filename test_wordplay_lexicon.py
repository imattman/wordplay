import pytest
import io
import wordplay

# a random sample of words from sowpods.txt
LEXICON_CONTENTS = """
COMPRISABLE
HOSES
HUSKLIKE
MOTUCAS
PHANEROPHYTE
PLAINCHANTS
POWDER
QUANTA
TACTUALITIES
WHIPPETS
""".strip()

EXPECTED_WORDS = [line.strip().lower() for line in LEXICON_CONTENTS.split()]


def test_read_words_empty_file():
    file_contents = io.StringIO('')
    words = wordplay.read_words(file_contents)
    assert [] == words


def test_read_words_normal():
    file_contents = io.StringIO(LEXICON_CONTENTS)
    words = wordplay.read_words(file_contents)
    assert EXPECTED_WORDS == words


def test_read_words_skip_empty_lines_and_comments():
    contents = LEXICON_CONTENTS.replace(
        '\n', '\n\n# some comment about a word\n')
    print("lexicon contents:", contents, sep='\n')  # `pytest -s` to see output
    file_contents = io.StringIO(contents)
    words = wordplay.read_words(file_contents)
    assert EXPECTED_WORDS == words
