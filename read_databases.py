import inspect
import time


def BAH(lat, lon, timestamp, depth):
    """Get data from the BAH database"""
    time.sleep(5)
    return (5.3, 6.7)


def NMHD(lat, lon, model):
    """Get data from the NHH database"""
    time.sleep(5)
    return (3.6, 8.9)


def LPMS(lat, lon, timestamp, style):
    """Get data from the LPMS database"""
    time.sleep(5)
    return (2.6, 4.6)


def read_databases(databases, **kwargs):
    """
    Given the list of databases to access and arguments to call into them,
    calls the functions with the relevant subset of the arguments passed and
    returns the sum of the first return value and the average of the second

    Examples:
        >>> read_databases(["BAH"], lat=4, lon=6, timestamp=57383, depth=5)
        (5.3, 6.7)

        >>> read_databases(["BAH", "LPMS"], lat=4, lon=6, timestamp=57383, depth=5, style="nadir")
        (7.9, 5.65)
    """
    responses = []
    for db in databases:
        fn = globals()[db]
        arg_names = set(inspect.signature(fn).parameters) & set(kwargs)
        args = {k: v for k,v in kwargs.items() if k in arg_names}
        res = fn(**args)
        responses.append(res)

    return (sum(r[0] for r in responses), sum(r[1] for r in responses)/len(responses))
