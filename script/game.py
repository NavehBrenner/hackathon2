from display import Display
import pygame as pg
from constants import *
from colors import *
from pygame import QUIT


class Game:
    def __init__(self) -> None:
        self.status = RUNNING  # init status to running
        self.screen = pg.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )  # create screen

    def run(self):
        pg.init()  # init pygame

        while self.status == RUNNING:
            for e in pg.event.get():
                if e.type == QUIT:
                    self.status = EXIT

            self.screen.fill(BASE_BG_COLOR)
            pg.display.flip()

        pg.quit()


game = Game()
game.run()
