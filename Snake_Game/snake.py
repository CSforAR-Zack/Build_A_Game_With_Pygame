from game_manager import GameManager
from snake_enums import Color, Direction
from square import Square


class Snake:
    """Class to manage the snake."""

    def __init__(self, gm: GameManager) -> None:
        self.gm: GameManager = gm
        self.head: Segment = Segment(self.gm, gm.center(), Direction.up)
        
        self.segments: list = [self.head]

    def draw(self) -> None:
        """Render the snake to the screen."""

        for segment in self.segments:        
            segment.draw()

    def move(self) -> None:
        """Move all segments forward thier direction."""

        for segment in self.segments:
            segment.x += segment.size * segment.direction[0]
            segment.y += segment.size * segment.direction[1]


class Segment(Square):
    """A class to represent a segment of the snake."""

    def __init__(
        self,
        gm: GameManager,
        pos: tuple,
        direction: Direction,
    ) -> None:
        
        super().__init__(gm, pos, Color.snake, direction)