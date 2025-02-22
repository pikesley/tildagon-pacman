from ...conf import sprite_data
from ...skin import Skin

data = sprite_data["pacman"]


class BlockyPacman(Skin):
    """A Pacman Skin."""

    def __init__(self, pacman):
        """Construct."""
        super().__init__(sprite=pacman)
        self.feet = "out"

        self.positions = ["wide", "narrow", "closed", "narrow"]
        self.positions_index = 2
        self.position = self.positions[self.positions_index]

    def animate(self):
        """Animate."""
        self.positions_index = (self.positions_index + 1) % len(self.positions)
        self.position = self.positions[self.positions_index]

    @property
    def pixels(self):
        """Draw."""
        pix = []

        self.start_y = self.sprite.anchor_y
        pix.extend(
            self.add_bits(
                data[self.sprite.facing][self.position],
                colours=[data["colours"]["shaded"], data["colours"]["primary"]],
            )
        )

        return pix
