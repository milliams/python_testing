from hypothesis import given
from hypothesis.strategies import lists, integers

from my_lib import add_elements


@given(lists(integers()), lists(integers()))
def test_add(a, b):
    add_elements(a, b)


# This is the fixed version of the my_lib function
def fixed_add_elements(a, b):
    """
    Given two lists, add them together elementwise and return the result
    """
    z = []
    for x, y in zip(a, b):
        z.append(x + y)
    return z
