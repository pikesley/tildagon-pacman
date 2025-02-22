import platform

if "MicroPython" in platform.platform():  # pragma: no cover
    from ..pikesley.shapes.rectangle import Rectangle
    from .tools import rgb_to_decimals

else:
    from lib.tools import rgb_to_decimals
    from pikesley.shapes.rectangle import Rectangle


class Skin:
    """A Skin."""

    def __init__(self, sprite):
        """Construct."""
        self.sprite = sprite

    def add_bits(self, source, colours=None):
        """Add some bits."""
        pix = []
        for bits in source:
            self.start_x = self.sprite.anchor_x
            for bit in bits:
                key, width = next(iter(bit.items()))
                for index, colour in enumerate(colours):
                    if int(key) == index + 1:
                        pix.append(self.pixel(colour, width))

                self.start_x += (self.sprite.scale * 2) * width
            self.start_y += self.sprite.scale * 2
        return pix

    def pixel(self, colour, width):
        """Generate one pixel."""
        return Rectangle(
            centre=(self.start_x, self.start_y),
            colour=rgb_to_decimals(colour),
            size=self.sprite.scale,
            width=width,
            opacity=self.sprite.opacity,
        )
