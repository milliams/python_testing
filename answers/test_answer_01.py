from my_lib import add_elements


def test_add():
    assert add_elements([1, 2], [3, 4]) == [4, 6]
