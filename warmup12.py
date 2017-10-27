#Astro Ohnuma
#10/27/17
#warmup12.py - finding greatest common factor

def GCF(num1,num2):
    for i in range(num1,0,-1):
        if num1%i==0 and num2%i==0:
            return i
print(GCF(10,15))