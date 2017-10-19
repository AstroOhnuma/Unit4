#Astro Ohnuma
#10/19/17
#monkeybanana.py - best game ever

from ggame import *


ROWS = 20
COLS = 40
CELL_SIZE = 20

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
    App().run()