from ...conf import sprite_data
from ...skin import Skin

data = sprite_data["ghost"]


class BlockyGhost(Skin):
    """A Ghost Skin."""

    def __init__(self, ghost):
        """Construct."""
        super().__init__(sprite=ghost)
        self.feet = "out"

    def animate(self):
        """Animate."""
        if self.feet == "out":
            self.feet = "in"
        else:
            self.feet = "out"

    @property
    def pixels(self):
        """Draw."""
        pix = []

        self.start_y = self.sprite.anchor_y
        colour = self.sprite.colour
        if self.sprite.is_blue:
            colour = data["colours"]["dead-face"]["body"]

        pix.extend(self.add_bits(data["core"], colours=[colour]))
        pix.extend(self.add_bits(data["feet"][self.feet], colours=[colour]))

        self.start_y = self.sprite.anchor_y

        if self.sprite.is_blue:
            pix.extend(
                self.add_bits(
                    data["dead-face"],
                    colours=[
                        data["colours"]["dead-face"]["eyes"],
                    ],
                )
            )
        else:
            pix.extend(
                self.add_bits(
                    data["eyes"][self.sprite.facing],
                    colours=[
                        data["colours"]["eyes"]["sclera"],
                        data["colours"]["eyes"]["pupil"],
                    ],
                )
            )

        return pix
