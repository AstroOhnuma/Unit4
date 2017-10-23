#Astro Ohnuma
#10/23/17
#localdemo.py - understanding local variables

def f():
    x = 77 #x is a local variable
    y = 10 #y is also a local variable

x = 5
f() #x does not change
print(x)
print(y) #this will cause an error]
