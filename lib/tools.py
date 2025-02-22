import platform


def is_tildagon():  # pragma: no cover
    """Are we running on a badge?"""
    return "MicroPython" in platform.platform()


def rgb_to_decimals(rgb):
    """RGB to decimals."""
    return [component / 255 for component in rgb]
