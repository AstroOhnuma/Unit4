#Astro Ohnuma
#10/19/17
#monkeybanana.py - best game ever

from ggame import *


ROWS = 20
COLS = 40
CELL_SIZE = 20

def moveright(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
    
def moveleft(event):
    if monkey.x > 0:
        monkey.x -= CELL_SIZE
    
def moveup(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
    
def movedown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y += CELL_SIZE
    
if __name__ == '__main__':
    
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    junglebox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeybox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananabox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    
    Sprite(junglebox)
    banana = Sprite(bananabox,(COLS*CELL_SIZE/2,ROWS*CELL_SIZE/2))
    monkey = Sprite(monkeybox)
    
    App().listenKeyEvent('keydown','right arrow', moveright)
    App().listenKeyEvent('keydown','left arrow', moveleft)
    App().listenKeyEvent('keydown','up arrow', moveup)
    App().listenKeyEvent('keydown','down arrow', movedown)
    App().run()
    