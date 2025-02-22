class Sprite:
    """A Sprite."""

    def __init__(  # noqa: PLR0913
        self,
        x=0,
        y=0,
        scale=6,
        facing="left",
        opacity=1.0,
        skin="blocky",
        name="dave",
    ):
        """Construct."""
        self.x = x
        self.y = y
        self.scale = scale
        self.opacity = opacity
        self.facing = facing
        self.skin = skin
        self.name = name

        self.set_anchors()

    def set_anchors(self):
        """Define anchor points."""
        self.anchor_y = self.start_y = (-self.scale * 10) + self.y
        self.anchor_x = self.x + (self.scale * -10)

    def move(self, direction, speed=2):
        """Move."""
        if direction == "up":
            self.y -= self.scale * speed
        if direction == "down":
            self.y += self.scale * speed
        if direction == "right":
            self.x += self.scale * speed
        if direction == "left":
            self.x -= self.scale * speed

    @property
    def is_visible(self):
        """Can we be seen?"""
        offset = self.scale * 11
        limit = 120 + offset

        return abs(self.x) < limit and abs(self.y) < limit
