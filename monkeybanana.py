#Astro Ohnuma
#10/19/17
#monkeybanana.py - best game ever

from ggame import *
from random import randint

#constants
ROWS = 20
COLS = 40
CELL_SIZE = 20

#moves the monkey right
def moveright(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            movebanana()
            updatescore()
#moves the monkey left            
def moveleft(event):
    if monkey.x > 0:
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            movebanana()
            updatescore()
#moves the monkey up
def moveup(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            movebanana()
            updatescore()
#moves monkey down 
def movedown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            movebanana()
            updatescore()
#moves banana to random location
def movebanana():
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
    data['frames'] = 0
#updates score when monkey gets banana
def updatescore():
    data['score'] += 10
    data['scoretext'].destroy()
    scorebox = TextAsset('Score = '+str(data['score']))
    data['scoretext'] = Sprite(scorebox,(0,ROWS*CELL_SIZE))
#keeps track of how many frames have passed
def step():
    data['frames'] += 1
    if data['frames'] == 30:
        movebanana()
#runs the game
if __name__ == '__main__':
    
    data = {}
    data['score'] = 0
    data['frames'] = 0
    
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    junglebox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeybox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananabox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    scorebox = TextAsset('Score = 0')
    
    Sprite(junglebox)
    banana = Sprite(bananabox,(COLS*CELL_SIZE/2,ROWS*CELL_SIZE/2))
    monkey = Sprite(monkeybox)
    data['scoretext'] = Sprite(scorebox, (0,ROWS*CELL_SIZE))
    
    App().listenKeyEvent('keydown','right arrow', moveright)
    App().listenKeyEvent('keydown','left arrow', moveleft)
    App().listenKeyEvent('keydown','up arrow', moveup)
    App().listenKeyEvent('keydown','down arrow', movedown)
    App().run(step)
    