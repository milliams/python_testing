import pytest
from my_lib import add_elements


@pytest.fixture
def pair_of_lists():
    return ([1, 2], [3, 4])


def test_add(pair_of_lists):
    list1 = pair_of_lists[0]
    list2 = pair_of_lists[1]
    assert add_elements(list1, list2) == [4, 6]
