#Astro Ohnuma
#10/19/17
#monkeybanana.py - best game ever

from ggame import *


ROWS = 40
COLS = 60
CELL_SIZE = 20

if __name__ == '__main__':
    
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    
    junglebox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeybox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    
    Sprite(junglebox)
    Sprite(monkeybox)
    
    App().run()
