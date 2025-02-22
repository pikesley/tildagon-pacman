from ..conf import sprite_data
from ..skins.pacman.blocky import BlockyPacman
from ..skins.pacman.smooth import SmoothPacman
from ..sprite import Sprite

data = sprite_data["pacman"]


class Pacman(Sprite):
    """A Pacman."""

    def __init__(  # noqa: PLR0913
        self,
        x=0,
        y=0,
        colour=(255, 0, 0),
        scale=6,
        facing="left",
        opacity=1.0,
        skin="blocky",
    ):
        """Construct."""
        super().__init__(
            x=x,
            y=y,
            scale=scale,
            facing=facing,
            opacity=opacity,
            skin=skin,
            name="pacman",
        )
        self.colour = colour

        self.is_blue = False

        self.skins = {
            "blocky": BlockyPacman(self),
            "smooth": SmoothPacman(self),
        }
        self.skin = self.skins[self.skin]

    @property
    def pixels(self):
        """Draw."""
        self.set_anchors()
        return self.skin.pixels

    def animate(self):
        """Animate."""
        return self.skin.animate()
