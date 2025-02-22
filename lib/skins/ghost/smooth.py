from math import radians

from ...conf import sprite_data
from ...skin import Skin
from ...tools import rgb_to_decimals

data = sprite_data["ghost"]


class SmoothGhost(Skin):
    """A  Ghost Skin."""

    def __init__(self, ghost):
        """Construct."""
        self.ghost = ghost
        self.feet = "out"

    def animate(self):
        """Animate."""

    @property
    def pixels(self):
        """Match the Sprite API."""
        return [self]

    def draw(self, ctx):
        """Draw."""
        ctx.rgb(*rgb_to_decimals(self.ghost.colour))
        if self.ghost.is_blue:
            ctx.rgb(*rgb_to_decimals(data["colours"]["dead-face"]["body"]))

        ctx.arc(
            self.ghost.x,
            self.ghost.y,
            # bitmaps are 11x11 pixels
            self.ghost.scale * 11,
            radians(180),
            radians(359.999),
            False,
        )
        ctx.line_to(
            self.ghost.x + (self.ghost.scale * 11),
            self.ghost.y + (self.ghost.scale * 9),
        )
        ctx.line_to(
            self.ghost.x - (self.ghost.scale * 11),
            self.ghost.y + (self.ghost.scale * 9),
        )

        ctx.close_path()
        ctx.fill()

        self.add_eyes(ctx)

    def add_eyes(self, ctx):
        """Draw an eye."""
        pupil_offsets = {
            "left": (-1, 0),
            "right": (1, 0),
            "up": (0, -1),
            "down": (0, 1),
        }

        for x_offset in [
            -data["smooth-eyes"]["separation"],
            data["smooth-eyes"]["separation"],
        ]:
            if self.ghost.is_blue:
                self.eye_part(
                    ctx,
                    data["colours"]["dead-face"]["eyes"],
                    x_offset * self.ghost.scale,
                    -self.ghost.scale * data["smooth-eyes"]["y-offset"],
                    data["smooth-eyes"]["radii"]["dead-eyes"],
                )
            else:
                self.eye_part(
                    ctx,
                    data["colours"]["eyes"]["sclera"],
                    x_offset * self.ghost.scale,
                    -self.ghost.scale * data["smooth-eyes"]["y-offset"],
                    data["smooth-eyes"]["radii"]["sclera"],
                )

                x_pupil_offset, y_pupil_offset = pupil_offsets[self.ghost.facing]
                self.eye_part(
                    ctx,
                    data["colours"]["eyes"]["pupil"],
                    (self.ghost.scale * x_offset) + (self.ghost.scale * x_pupil_offset),
                    -(self.ghost.scale * data["smooth-eyes"]["y-offset"])
                    + (self.ghost.scale * y_pupil_offset),
                    data["smooth-eyes"]["radii"]["pupil"],
                )

    def eye_part(self, ctx, colour, x, y, radius):
        """Draw an eye part."""
        ctx.rgb(*rgb_to_decimals(colour))
        ctx.arc(
            self.ghost.x + x,
            self.ghost.y + y,
            self.ghost.scale * radius,
            radians(0),
            radians(359.999),
            False,
        )
        ctx.fill()
