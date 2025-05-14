class Color:
    """Color class to store RGB values for a color."""

    bg: tuple = (0, 0, 0)
    text: tuple = (237, 182, 43)


class FontFiles:
    """Font class to hold all font files."""

    large: str = "fonts/Kenney_Future.ttf"
    small: str = "fonts/Kenney_Future.ttf"
    

class State:
    """State class to represent the games states."""

    menu: int = 0
    in_game: int = 1
    game_over: int = 2
    end_game: int = 3

    def next_state(state: int) -> int:
        """Get the next state."""

        state = (state + 1) % 3
        return state