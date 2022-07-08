import inspect


def framemetric():
    """How far in the caller is, in frames."""
    s = ''
    f = inspect.currentframe().f_back

    while f is not None:
        s += '    '
        f = f.f_back

    return s + '|'
