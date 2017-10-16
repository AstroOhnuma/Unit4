#Astro Ohnuma
#10/16/17
#printstars.py - takes and integer and then prints out that many stars

def printnstars(num1):
    total = num1
    for i in range(1,num1+1):
        total -= 1
        print((i*'*'),(total*' '))

printnstars(6)
