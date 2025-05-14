import sys

import pygame as pg

from game_manager import GameManager
from snake import Snake
from snake_enums import Color, Direction, State


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
        gm.screen.fill(Color.bg)
        menu_text(gm)
        pg.display.flip()


def game_loop(gm: GameManager) -> None:
    """The main game loop."""

    snake: Snake = Snake(gm)

    while gm.state == State.in_game:
        gm.tick()
        process_events(gm, snake)

        snake.move()

        # Update the screen
        gm.screen.fill(Color.bg)
        snake.draw()
        score_text(gm)
        pg.display.flip()


def game_over_loop(gm: GameManager) -> None:
    """The game over loop."""

    while gm.state == State.game_over:
        process_events(gm)

        # Update the screen
        gm.screen.fill(Color.bg)
        game_over_text(gm)
        score_text(gm)
        pg.display.flip()


def process_events(gm: GameManager, snake: Snake=None) -> None:
    """Process events for the game."""

    for event in pg.event.get():
        if event.type == pg.QUIT:
            gm.state = State.end_game
            break

        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            gm.state = State.next_state(gm.state)
            break

        if snake is not None and event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and snake.head.direction != Direction.down:
                snake.head.direction = Direction.up
            elif event.key == pg.K_DOWN and snake.head.direction != Direction.up:
                snake.head.direction = Direction.down
            elif event.key == pg.K_RIGHT and snake.head.direction != Direction.left:
                snake.head.direction = Direction.right
            elif event.key == pg.K_LEFT and snake.head.direction != Direction.right:
                snake.head.direction = Direction.left


def menu_text(gm: GameManager) -> None:
    """Display the menu text."""

    gm.screen.blit(
        gm.large_font.render(">-<8==SNAKE==>", True, Color.text),
        (gm.width * .2, gm.height * .45, gm.width, gm.height),
    )
    gm.screen.blit(
        gm.small_font.render("Press Enter to play.", True, Color.text),
        (gm.width * .3, gm.height * .55, gm.width, gm.height),
    )


def score_text(gm: GameManager) -> None:
    """Display the game text."""
    
    gm.screen.blit(
        gm.small_font.render(f"Score: {gm.score}", True, Color.text),
        (gm.width * .1, gm.height * .04, gm.width, gm.height),
    )
    gm.screen.blit(
        gm.small_font.render(f"High Score: {gm.high_score}", True, Color.text),
        (gm.width * .60, gm.height * .04, gm.width, gm.height),
    )


def game_over_text(gm: GameManager) -> None:
    """Display the game over text."""

    gm.screen.blit(
        gm.large_font.render("GAME OVER", True, Color.text),
        (gm.width * .29, gm.height * .45, gm.width, gm.height),
    )
    gm.screen.blit(
        gm.small_font.render("Press Enter to play again.", True, Color.text),
        (gm.width * .23, gm.height * .55, gm.width, gm.height),
    )


if __name__ == "__main__":
    main()
