#Astro Ohnuma
#10/26/17
#recursiondemo.py - A recursive version of the countdown function

def countdown(n):
    if n == 0:
        print('Boom!')
    else:
        print(n)
        countdown(n-1)
        
countdown(5)
