#Astro Ohnuma
#10/23/17
#programlist2functions.py - the functions for program list 2

#8 - taking two strings as arguments and returns a string that contains all the letters that appear in at least one of the words
"""
def stringunion(str1,str2):
    answer = ''
    for ch in str1:
        if not ch in answer:
            answer += ch
    for ch in str2:
        if not ch in answer:
            answer += ch
    print(answer)
stringunion('Mississipi','Pensylvania')
"""
#9 - taking two strings as arguments and returns a string that contains all the letters that are in both the first and second word
def stringintersect(str1,str2):
    answer = ''
    for ch in str1:
        if ch in answer:
            answer += ch
    for ch in str2:
        if ch in answer:
            answer += ch
    print(answer)
stringintersect('Mississipi','Pensylvania')
