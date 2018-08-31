import read_databases


def test_single(mocker):
    mocker.patch('read_databases.BAH', return_value=(5.3, 6.7))
    res = read_databases.read_databases(["BAH"], lat=4, lon=6, timestamp=57383, depth=5)

    read_databases.BAH.assert_called_once()
    assert res == (5.3, 6.7)


def test_multiple(mocker):
    mocker.patch('read_databases.BAH', return_value=(5.3, 6.7))
    mocker.patch('read_databases.LPMS', return_value=(2.6, 4.6))
    res = read_databases.read_databases(["BAH", "LPMS"], lat=4, lon=6, timestamp=57383, depth=5, style="nadir")

    read_databases.BAH.assert_called_once()
    read_databases.LPMS.assert_called_once()
    assert res == (7.9, 5.65)
