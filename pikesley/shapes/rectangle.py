from .shape import Shape


class Rectangle(Shape):
    """A rectangle."""

    def draw_lines(self, ctx):
        """Draw ourself."""
        ctx.move_to((self.size * self.width * 2) - self.size, -self.size)
        ctx.line_to((self.size * self.width * 2) - self.size, self.size)
        ctx.line_to(-self.size, self.size)
        ctx.line_to(-self.size, -self.size)

        ctx.close_path()
