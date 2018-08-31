import lzma
import pytest
from my_lib import get_gutenberg_text, word_count


@pytest.fixture(scope='module')
def warandpeace():
    with lzma.open('warandpeace.txt.xz', mode='rt') as f:
        text = f.read()
    book_text = get_gutenberg_text(text)
    return book_text


def test_count_lines(warandpeace):
    assert len(warandpeace.split('\n')) == 65678


@pytest.mark.parametrize('word,count',  [
    ('hat', 33),
    ('freedom', 71),
    ('electricity', 1),
    ('testing', 3),
    ('Prince', 1498),
    ('', 563297),
])
def test_word_counts(warandpeace, word, count):
    assert word_count(warandpeace, word) == count

