# Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka parameter lega aur
# 0 se limit tak ke beech ke sabhi even aur odd numbers ko label ke saath print karega jaisa ki 
# niche dikhaya gaya hai.
def showNumbers(limit):
    i=0
    while i<limit:
        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
        i=i+1
showNumbers(10)


