import pygame
import time
import random

class Fruit():
    def fruitPosition():
        pass


class Snake():
    windowSizeX = 720
    windowSizeY = 480
    # default snake position
    snakePosition = [100, 50]
    snakeBody = [
                 [100, 50],
                 [90,  50],
                 [80,  50],
                 [70,  50]
                ]
    # set the fruit position randomly on the screen
    fruitPosition = [random.randrange(1, (windowSizeX // 10)) * 10,
                     random.randrange(1, (windowSizeY //10))  * 10]
    fruitSpawn = True
    # Set the default player directions
    playerDirection = 'RIGHT'
    changeTo = playerDirection
    # Player's score
    score = 0
    # initialize pygame
    pygame.init()

    # initialize game window
    pygame.display.set_caption("Python Snakes")
    gameWindow = pygame.display.set_mode((windowSizeX, windowSizeY))

    # frames per second controller
    fps = pygame.time.Clock()

    def __init__(self) -> None:
        snakeSpeed = 15
        windowSizeX = 720
        windowSizeY = 480
        # RGB ocolors
        black = pygame.color(0, 0 , 0)
        white = pygame.Color(255, 255, 255)
        red = pygame.Color(255, 0, 0)
        green = pygame.Color(0, 255, 0)
        blue = pygame.Color(0, 0, 255)

    def snakeHelper(self):
        # initialize pygame
        pygame.init()

        # initialize game window
        pygame.display.set_caption("Python Snakes")
        gameWindow = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))

        # frames per second controller
        fps = pygame.time.Clock()

    def showScore(self, choice, color, font, size):
        # font object for the score
        scoreFont = pygame.font.SysFont(font, size)
        # create the display for the surface of the game 
        scoreSurface = scoreFont.render('Score: ' + str(self.score), True, color)
        # rectangle object for the surface object
        scoreRectangle = scoreSurface.get_rect()
        # display the text
        self.gameWindow.blit(scoreSurface, scoreRectangle)
    
    def gameOver(self):
        myFont = pygame.font.SysFont('times new roman', 50)
        # create the surface for the game over screen
        gameOverSurface = myFont.render("Your Score is: " + str(self.score), True)
        # create rectangle for the game over
        gameOverRect = gameOverSurface.get_rect()


        

def main() -> None:
    # Initialize Snake class
    mySnakeGame = Snake()


if __name__ == "__name__":
    main()