from lib.sprite import Sprite


def test_default_sprite():
    """Test."""
    spr = Sprite()

    assert spr.x == 0
    assert spr.anchor_x == -60


def test_configured_sprite():
    """Test."""
    spr = Sprite(x=-10, y=20, scale=3)

    assert spr.anchor_y == -10


def test_moving_sprite():
    """Test."""
    spr = Sprite()

    assert spr.x == 0
    assert spr.y == 0

    spr.move("left")
    spr.move("down", speed=3)

    assert spr.x == -12


def test_visibility():
    """Test it knows when it's visible."""
    spr = Sprite(x=0, y=0, scale=1)
    assert spr.is_visible

    spr.x = -150
    assert not spr.is_visible

    spr.x = 132
    assert not spr.is_visible

    spr.y = 132
    assert not spr.is_visible

    spr.y = -150
    assert not spr.is_visible

    spr.scale = 6
    spr.x = 140
    assert spr.is_visible
