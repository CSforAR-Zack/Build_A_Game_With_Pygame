import sys

import pygame as pg

from game_manager import GameManager
from snake_enums import State


def main():
    # Main game setup and game loop logic goes here
    pg.init()

    gm: GameManager = GameManager()

    pg.display.set_caption("Snake")

    while gm.state != State.end_game:
        menu_loop(gm)
        game_loop(gm)
        game_over_loop(gm)

    pg.quit()
    sys.exit()


def menu_loop(gm: GameManager) -> None:
    """The main menu loop."""

    while gm.state == State.menu:
        process_events(gm)

        # Update the screen
        gm.screen.fill((0, 255, 0))
        pg.display.flip()


def game_loop(gm: GameManager) -> None:
    """The main game loop."""

    while gm.state == State.in_game:
        process_events(gm)

        # Update the screen
        gm.screen.fill((0, 0, 255))
        pg.display.flip()


def game_over_loop(gm: GameManager) -> None:
    """The game over loop."""

    while gm.state == State.game_over:
        process_events(gm)

        # Update the screen
        gm.screen.fill((255, 0, 0))
        pg.display.flip()


def process_events(gm: GameManager) -> None:
    """Process events for the game."""

    for event in pg.event.get():
        if event.type == pg.QUIT:
            gm.state = State.end_game
            break

        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            gm.state = State.next_state(gm.state)
            break


if __name__ == "__main__":
    main()
