from morse import encode, decode


def test_sos():
    assert encode('sos') == '... --- ...'


def test_decode_sos():
    assert decode('... --- ...') == 'sos'
