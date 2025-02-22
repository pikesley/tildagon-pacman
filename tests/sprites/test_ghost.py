from lib.sprites.ghost import Ghost


def test_simple_ghost():
    """Test."""
    gst = Ghost()

    assert gst.colour == (255, 0, 0)
