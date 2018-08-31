import pytest

from my_lib import add_elements


@pytest.mark.parametrize("a, b, answer", [
    ([1, 2], [3, 4], [4, 6]),
])
def test_add(a, b, answer):
    assert add_elements(a, b) == answer

