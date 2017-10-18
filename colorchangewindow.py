#Astro Ohnuma
#10/16/17
#colorchangewindow.py - pops up a window that changes to a random color every time you click it

from ggame import *

def mouseclick(event):
    red = Color(0xFF0000,1)
    green = Color(0x00FF00,1)
    blue = Color(0x0000FF,1)
    black = Color(0x000000,1)
    blackoutline = LineStyle(1,black)