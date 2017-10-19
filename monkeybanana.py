#Astro Ohnuma
#10/19/17
#monkeybanana.py - best game ever

from ggame import *


ROWS = 20
COLS = 40
CELL_SIZE = 20

def moveright(event):
    monkey.x += CELL_SIZE
    
def moveleft(event):
    monkey.x -= CELL_SIZE
    
def moveup(event):
    monkey.y -= CELL_SIZE
    
def movedown(event):
    monkey.y += CELL_SIZE
    
if __name__ == '__main__':
    
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    junglebox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeybox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananabox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    
    Sprite(junglebox)
    monkey = Sprite(monkeybox)
    Sprite(bananabox,(COLS*CELL_SIZE/2,ROWS*CELL_SIZE/2))
    
    App().listenKeyEvent('keydown','right arrow', moveright)
    App().listenKeyEvent('keydown','left arrow', moveleft)
    App().listenKeyEvent('keydown','up arrow', moveup)
    App().listenKeyEvent('keydown','down arrow', movedown)
    App().run()