#Astro Ohnuma
#10/20/17
#distance.py - takes two points as agruements and returns the distance between the two points
from math import sqrt

def distance(x1,y1,x2,y2):
    total = sqrt((x2-x1)**2+(y2-y1)**2)
    return total
    
print(distance(3,4,-5,2))
