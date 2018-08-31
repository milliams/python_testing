from my_lib import count_capital_words_in_website

from types import SimpleNamespace


def test_count_words(mocker):
    get = mocker.patch("requests.get", return_value=SimpleNamespace(text="a Set of words With some Capitals"))

    assert count_capital_words_in_website("http://example.com") == 3
    get.assert_called_once()
