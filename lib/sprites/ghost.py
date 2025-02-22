from ..conf import sprite_data
from ..skins.ghost.blocky import BlockyGhost
from ..skins.ghost.smooth import SmoothGhost
from ..sprite import Sprite

data = sprite_data["ghost"]


class Ghost(Sprite):
    """A Ghost."""

    def __init__(  # noqa: PLR0913
        self,
        x=0,
        y=0,
        colour=(255, 0, 0),
        scale=6,
        facing="left",
        opacity=1.0,
        skin="blocky",
        name="dave",
    ):
        """Construct."""
        super().__init__(
            x=x, y=y, scale=scale, facing=facing, opacity=opacity, skin=skin, name=name
        )
        self.colour = colour

        self.is_blue = False

        self.skins = {
            "blocky": BlockyGhost(self),
            "smooth": SmoothGhost(self),
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
