from math import radians

from ...conf import sprite_data
from ...skin import Skin
from ...tools import rgb_to_decimals

data = sprite_data["pacman"]

centres = {"left": 180, "right": 360, "up": 270, "down": 90}


class SmoothPacman(Skin):
    """Smooth Pacman."""

    def __init__(self, ghost):
        """Construct."""
        super().__init__(sprite=ghost)

        self.spacings = [0, 15, 30, 45, 45, 30, 15, 0]
        self.spacings_index = 0
        self.spacing = self.spacings[self.spacings_index]

    def animate(self):
        """Animate."""
        self.spacings_index = (self.spacings_index + 1) % len(self.spacings)
        self.spacing = self.spacings[self.spacings_index]

    @property
    def pixels(self):
        """Match the Sprite API."""
        return [self]

    def draw(self, ctx):
        """Draw."""
        ctx.rgb(*rgb_to_decimals(data["colours"]["primary"]))

        points = (
            (centres[self.sprite.facing] + self.spacing, 359.999),
            (0, centres[self.sprite.facing] - self.spacing),
        )

        if self.sprite.facing == "right":
            points = (
                (
                    self.spacing,
                    360 - self.spacing,
                ),
            )

        for start, end in points:
            for command in [ctx.stroke, ctx.fill]:
                ctx.arc(
                    self.sprite.x,
                    self.sprite.y,
                    # bitmaps are 11x11 pixels
                    self.sprite.scale * 11,
                    radians(end),
                    radians(start),
                    True,
                )
                ctx.line_to(self.sprite.x, self.sprite.y)
                command()
