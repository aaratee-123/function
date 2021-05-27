# Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski length
# jyaada hogi use print karega aur agar dono strings ki length equal hui to dono ko line by line
# print karega . Hint :- use len() builtin function.. 

def fun(a,b):
    i=0
    while i<1:
        j=0
        while j<1:
            j=j+1
        i=i+1
        if len(a)>len(b):
            print(a)
        elif len(b)>len(a):
            print(b)
        else:
            print(a,b)
fun(["a","b","c"],["p","q"])