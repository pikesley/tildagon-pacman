from unittest.mock import MagicMock, call

from lib.sprites.pacman import Pacman


def test_drawing():
    """Test."""
    pac = Pacman(skin="smooth", scale=1.0)
    mock_ctx = MagicMock()

    pac.skin.draw(mock_ctx)

    assert mock_ctx.rgb.mock_calls == [call(1.0, 1.0, 0.1411764705882353)]
    assert mock_ctx.arc.mock_calls == [  # two arcs, stroke and fill each
        call(0, 0, 11.0, 6.283167853887067, 3.141592653589793, True),
        call(0, 0, 11.0, 6.283167853887067, 3.141592653589793, True),
        call(0, 0, 11.0, 3.141592653589793, 0.0, True),
        call(0, 0, 11.0, 3.141592653589793, 0.0, True),
    ]

    assert mock_ctx.line_to.mock_calls == [
        call(0, 0),
        call(0, 0),
        call(0, 0),
        call(0, 0),
    ]

    assert mock_ctx.fill.call_count == 2
    assert mock_ctx.stroke.call_count == 2


def test_animation():
    """Test."""
    pac = Pacman(skin="smooth", scale=3.0, facing="up")
    mock_ctx = MagicMock()

    pac.move("up")
    pac.animate()
    pac.skin.draw(mock_ctx)

    assert mock_ctx.arc.mock_calls == [
        call(0, -6.0, 33.0, 6.283167853887067, 4.974188368183839, True),
        call(0, -6.0, 33.0, 6.283167853887067, 4.974188368183839, True),
        call(0, -6.0, 33.0, 4.4505895925855405, 0.0, True),
        call(0, -6.0, 33.0, 4.4505895925855405, 0.0, True),
    ]

    assert mock_ctx.line_to.mock_calls == [
        call(0, -6),
        call(0, -6),
        call(0, -6),
        call(0, -6),
    ]

    assert mock_ctx.fill.call_count == 2
    assert mock_ctx.stroke.call_count == 2


def test_facing_right():
    """Test this special case."""
    pac = Pacman(skin="smooth", scale=1.0, facing="right")
    mock_ctx = MagicMock()

    pac.skin.draw(mock_ctx)

    assert mock_ctx.arc.mock_calls == [
        call(0, 0, 11.0, 6.283185307179586, 0.0, True),
        call(0, 0, 11.0, 6.283185307179586, 0.0, True),
    ]

    assert mock_ctx.line_to.mock_calls == [
        call(0, 0),
        call(0, 0),
    ]

    assert mock_ctx.fill.call_count == 1
    assert mock_ctx.stroke.call_count == 1


def test_pixels():
    """Test it implements the `pixels` API."""
    pac = Pacman(skin="smooth")

    assert pac.pixels[0].__class__.__name__ == "SmoothPacman"
