

i=0

def word_count(str,n):
    i=0
    counts = dict()
    words = str.split()
    

    for word in words:
        if len(word)==n:
           i += 1
       

    return i


m=input("enter sentence : ")
n=int(input("enter number : "))


print( word_count(m,n))
