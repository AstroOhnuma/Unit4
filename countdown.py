#Astro Ohnuma
#10/16/17
#countdownn.py - taking an integer and counting down to zero from that number

def countdownn(num1):
    i = num1
    while i >=1:
        print(i)
        i -= 1
    print('BOOM!')

countdownn(10)