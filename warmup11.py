#Astro Ohnuma
#10/23/17
#warmup11.py - determine if a number is prime and print True or False

def isprime(x):
    i = 1
    while i < x:
        i += 1
    if x%i==0:
        return False
    else:
        return True
    

print(isprime(7))