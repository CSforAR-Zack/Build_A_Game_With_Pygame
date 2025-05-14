import pygame as pg

from snake_enums import State


class GameManager:
    """Manages the game and state."""

    # Make GameManager a singleton
    _instance: "GameManager" = None

    def __new__(cls) -> "GameManager":
        """Singleton pattern to ensure only one instance of GameManager exists."""

        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        """Initializes the game manager."""
        
        self.width: int = 800
        self.height: int = self.width
        self.screen: pg.Surface = pg.display.set_mode((self.width, self.height))

        self.state: int = State.menu