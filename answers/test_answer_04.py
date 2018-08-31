import pytest

from my_lib import add_elements


def test_wrong_type():
    with pytest.raises(TypeError):
        add_elements([1, 2], 6)
