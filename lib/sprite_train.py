from .conf import conf, sprite_data
from .sprites.ghost import Ghost
from .sprites.pacman import Pacman


class SpriteTrain:
    """Train of Sprites."""

    def __init__(self, scale=conf["player"]["scale"]["default"], skin="blocky"):
        """Construct."""
        self.scale = scale
        self.skin = skin

        self.ghosts = [
            Ghost(
                name=name,
                colour=ghost["colour"],
                scale=self.scale,
                skin=self.skin,
            )
            for name, ghost in sprite_data["ghost"]["ghosts"].items()
        ]
        self.pacman = Pacman(scale=self.scale, skin=self.skin)

        self.chaser = "ghosts"

        self.reorder()
        self.rescale(self.scale)
        self.align()

    def rescale(self, scale):
        """Rescale everything."""
        self.scale = scale
        for sprite in self.sprites:
            sprite.scale = self.scale

        self.spacing = conf["sprite-spacing"] * (11 * 2 * self.scale)

    def reorder(self):
        """Line ourselves up."""
        # TODO fix spacing here
        if self.chaser == "ghosts":
            self.sprites = [self.pacman] + self.ghosts
        else:
            self.sprites = self.ghosts + [self.pacman]

    def recolour(self):
        """Recolour the ghosts."""
        for ghost in self.ghosts:
            ghost.is_blue = self.chaser == "pacman"

    def align(self, direction="right", offset=None):
        """Set the positions of each."""
        if not offset and offset != 0:
            offset = 120 + (11 * self.scale)
        for index, sprite in enumerate(self.sprites):
            sprite.facing = direction

            if direction == "down":  # pragma: no cover
                sprite.x = 0
                sprite.y = (index * -self.spacing) - offset
            if direction == "up":
                sprite.x = 0
                sprite.y = (index * self.spacing) + offset
            if direction == "right":
                sprite.x = (index * -self.spacing) - offset
                sprite.y = 0
            if direction == "left":  # pragma: no cover
                sprite.x = (index * self.spacing) + offset
                sprite.y = 0

    def move(self, direction, speed=2):
        """Move everybody."""
        for sprite in self.sprites:
            sprite.move(direction=direction, speed=speed)

    @property
    def off_screen(self):
        """Is the whole train off-screen?"""
        return not any(sprite.is_visible for sprite in self.sprites)
