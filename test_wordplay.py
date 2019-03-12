import pytest
import wordplay


@pytest.mark.parametrize("word, score", [
    ('', 0),
    ('a', 1),
    ('bird', 7),
    ('cat', 5),
    ('fish', 10),
    ('bliffy', 17),
    ('xylophone', 24),
    ('leet-speak', 15),
    ('l33t-sp34k', 11),
])
def test_score_word(word, score):
    assert wordplay.score_word(word) == score


def test_empty_lexicon_has_zero_len():
    lex = wordplay.Lexicon([])
    assert len(lex) == 0


def test_lexicon_word_membership():
    words = ['apple', 'orange', 'banana', 'blueberry']
    lex = wordplay.Lexicon(words)

    assert len(lex) == len(words)

    for word in words:
        assert word in lex
        score = wordplay.score_word(word)
        assert lex.get_word(word) == (score, word)

    for missing in ['one', 'two', 'red', 'blue', 'fish']:
        assert missing not in lex
        assert lex.get_word(missing) is None
