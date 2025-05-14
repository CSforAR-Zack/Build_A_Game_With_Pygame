from game_manager import GameManager
from snake_enums import Color
from square import Square


class Snake:
    """Class to manage the snake."""

    def __init__(self, gm: GameManager) -> None:
        self.gm: GameManager = gm
        self.head: Segment = Segment(self.gm, gm.center())
        
        self.segments: list = [self.head]

    def draw(self) -> None:
        """Render the snake to the screen."""

        for segment in self.segments:        
            segment.draw()


class Segment(Square):
    """A class to represent a segment of the snake."""

    def __init__(
        self,
        gm: GameManager,
        pos: tuple,
    ) -> None:
        
        super().__init__(gm, pos, Color.snake)