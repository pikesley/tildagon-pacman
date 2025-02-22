from unittest.mock import MagicMock, call

from lib.sprites.ghost import Ghost


def test_drawing():
    """Test."""
    gst = Ghost(skin="smooth", scale=1.0)
    mock_ctx = MagicMock()

    gst.skin.draw(mock_ctx)

    assert mock_ctx.rgb.mock_calls == [
        call(1.0, 0.0, 0.0),  # body
        call(0.8509803921568627, 0.8509803921568627, 0.8509803921568627),  # sclera
        call(0.054901960784313725, 0.01568627450980392, 0.996078431372549),  # pupil
        call(0.8509803921568627, 0.8509803921568627, 0.8509803921568627),  # sclera
        call(0.054901960784313725, 0.01568627450980392, 0.996078431372549),  # pupil
    ]

    assert mock_ctx.arc.mock_calls == [
        call(0, 0, 11.0, 3.141592653589793, 6.283167853887067, False),  # head
        call(-4.0, -2.0, 3.0, 0.0, 6.283167853887067, False),  # sclera
        call(-5.0, -2.0, 1.0, 0.0, 6.283167853887067, False),  # pupil
        call(4.0, -2.0, 3.0, 0.0, 6.283167853887067, False),  # sclera
        call(3.0, -2.0, 1.0, 0.0, 6.283167853887067, False),  # pupil
    ]

    assert mock_ctx.line_to.mock_calls == [
        call(11.0, 9.0),  # down
        call(-11.0, 9.0),  # across
    ]

    mock_ctx.close_path.assert_called_with()
    mock_ctx.fill.assert_called_with()


def test_moving():
    """Test."""
    gst = Ghost(skin="smooth", scale=2.0)
    mock_ctx = MagicMock()

    gst.move("right", speed=3)
    gst.skin.draw(mock_ctx)

    assert mock_ctx.rgb.mock_calls == [
        call(1.0, 0.0, 0.0),  # body
        call(0.8509803921568627, 0.8509803921568627, 0.8509803921568627),  # sclera
        call(0.054901960784313725, 0.01568627450980392, 0.996078431372549),  # pupil
        call(0.8509803921568627, 0.8509803921568627, 0.8509803921568627),  # sclera
        call(0.054901960784313725, 0.01568627450980392, 0.996078431372549),  # pupil
    ]

    assert mock_ctx.arc.mock_calls == [
        call(6.0, 0, 22.0, 3.141592653589793, 6.283167853887067, False),
        call(-2.0, -4.0, 6.0, 0.0, 6.283167853887067, False),
        call(-4.0, -4.0, 2.0, 0.0, 6.283167853887067, False),
        call(14.0, -4.0, 6.0, 0.0, 6.283167853887067, False),
        call(12.0, -4.0, 2.0, 0.0, 6.283167853887067, False),
    ]

    assert mock_ctx.line_to.mock_calls == [
        call(28.0, 18.0),  # down
        call(-16.0, 18.0),  # across
    ]

    mock_ctx.close_path.assert_called_with()
    mock_ctx.fill.assert_called_with()


def test_pixels():
    """Test it implements the `pixels` API."""
    gst = Ghost(skin="smooth", scale=2.0)

    assert gst.pixels[0].__class__.__name__ == "SmoothGhost"


def test_blue_ghost():
    """Test."""
    gst = Ghost(scale=3, facing="down", skin="smooth")
    mock_ctx = MagicMock()

    gst.is_blue = True
    gst.skin.draw(mock_ctx)

    mock_ctx.rgb.assert_called_with(0.9803921568627451, 0.6588235294117647, 1.0)
