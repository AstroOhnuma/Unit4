#Astro Ohnuma
#10/18/17
#printsquares.py - printing squares with a function

def printsquares(num1,num2):
    for i in range(1,num2):
        print(('+--'*num2)+('+'))
        print(('|  |  '*num1)+('|'))
    print(('+--'*num2)+('+'))
    


printsquares(3,4)