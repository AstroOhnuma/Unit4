#Astro Ohnuma
#10/16/17
#colorchangewindow.py - pops up a window that changes to a random color every time you click it

from ggame import *
from random import randint

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
blackoutline = LineStyle(1,black)
    
redbackground = RectangleAsset(600,600,blackoutline,red)
greenbackground = RectangleAsset(600,600,blackoutline,green)
bluebackground = RectangleAsset(600,600,blackoutline,blue)

def mouseclick(event):
    num = randint(1,3)
    if num == 1:
        Sprite(redbackground)
    elif num == 2:
        Sprite(greenbackground)
    elif num == 3:
        Sprite(bluebackground)
    App().listenMouseEvent('click', mouseclick)
    App().run()
    