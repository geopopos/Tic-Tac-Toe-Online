import pygame, math
from pygame.locals import *

w = 480
h = 480
tileSize = ((w/3 - 20), (h/3 - 20))

def drawX(screen, boardPos, size):
    #draw a x at the board position
    pygame.draw.lines(screen, (240, 20, 20), False, [(boardPos[0], boardPos[1]), ((boardPos[0] + size[0]), (boardPos[1] + size[1]))], 3)
    pygame.draw.lines(screen, (240, 20, 20), False, [(boardPos[0] + size[0], boardPos[1]), ((boardPos[0]), (boardPos[1] + size[1]))], 3)    
    
def drawO(screen, boardPos, size):
    #draw a y at the board position
    pygame.draw.ellipse(screen, (20, 20, 240), [boardPos[0], boardPos[1], size[0], size[1]], 3)
    
class Pointer:
    def __init__(self, screen):
        self.on = True
        self.screen = screen
        self.sprite = "x"
        self.size = (20, 20)
        self.position = (0, 0)

    def setPosition(self, position):
        self.position = (position[0] - (self.size[0]/2), position[1] - (self.size[1]/2) )

    def display(self):
        drawX(self.screen, self.position, self.size)
        
class Game():
    def __init__(self):
        self.running = True
        self.winner = None
        self.turn = 0
    
class Board():
    def __init__(self, screen):
        self.screen = screen
        self.boardArray = [" " for x in range(9)]
        self.boardPositions = []
        for i in range(9):
            self.boardPositions.append((int((i%3) * (w/3)) + 10, int(math.floor(i/3) * (h/3)) + 10))
        print(self.boardPositions[0][0])

    def setMarker(self, marker, mousePos):
        mouseRect = pygame.Rect(mousePos[0], mousePos[1], 1, 1)
        for i in range(9):
            boardRect = pygame.Rect(self.boardPositions[i][0], self.boardPositions[i][1], tileSize[0], tileSize[1])
            if boardRect.colliderect(mouseRect):
                self.boardArray[i] = marker
            
            
    def display(self):
        #draw function for board background, outline, and X\O sprites
        pygame.draw.lines(self.screen, (20, 20, 20), False, [(0, (h/3)), (w, (h/3))])
        pygame.draw.lines(self.screen, (20, 20, 20), False, [(0, ((h/3)*2)), (w, ((h/3)*2))])
        pygame.draw.lines(self.screen, (20, 20, 20), False, [((w/3), 0), ((w/3), h)])
        pygame.draw.lines(self.screen, (20, 20, 20), False, [((w/3)*2, 0), ((w/3)*2, h)])        
        for i in range(9):
            pygame.draw.rect(self.screen, (255, 255, 255), (self.boardPositions[i][0],self.boardPositions[i][1], tileSize[0], tileSize[1]));
            if self.boardArray[i] == "x":
                drawX(self.screen, self.boardPositions[i], tileSize)
            if self.boardArray[i] == "o":
                drawO(self.screen, self.boardPositions[i], tileSize)
            
def processInput():
    #process player input
    #loop over input events
    for event in pygame.event.get():
        #Check if player has pressed escape key if so quit the game
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            game.running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            board.setMarker("x", pygame.mouse.get_pos())

def update():
    #update variables
    pointer.setPosition(pygame.mouse.get_pos())

def render():
    #render graphics
    screen.fill((240, 240, 240))
    board.display()
    pointer.display()
    pygame.display.update()
    
if __name__ == "__main__":
    pygame.init()
    pygame.mouse.set_visible(0)
    game = Game()

    screen = pygame.display.set_mode((w, h))
    
    board = Board(screen)
    pointer = Pointer(screen)
    
    while game.running:
        processInput()
        update()
        render()


    pygame.quit()
