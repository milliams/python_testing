import string

from hypothesis import given
import hypothesis.strategies as st

from morse import encode, decode, letter_to_morse


@given(st.text(alphabet=string.ascii_letters + string.digits))
def test_roundtrip(text):
    assert decode(encode(text)) == text


@given(st.lists(elements=st.sampled_from(list(letter_to_morse.values()))))
def test_roundtrip_morse(morse):
    morse_message = ' '.join(morse)
    assert encode(decode(morse_message)) == morse_message
