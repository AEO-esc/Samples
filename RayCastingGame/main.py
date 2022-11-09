import pygame as pg
import sys
from settings import *
from map import *

class Game:
    def __init__(self) -> None:
        # initialize pygame
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.newGame()
    
    def newGame(self):
        # initialize a new map
        #self.map = Map(self)
        pass

    def update(self):
        # update the FPS on the screen
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
    
    def draw(self):
        # fill the screen with black
        self.screen.fill('black')
        #self.map.draw()
    
    def checkEvents(self):
        for event in pg.event.get():
            # close the game if the player selects quit or the escape key
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        # main loop for game
        while True:
            self.checkEvents()
            self.update()
            self.draw()

if __name__ == "__main__":
    # initialize class & run
    game = Game()
    game.run()