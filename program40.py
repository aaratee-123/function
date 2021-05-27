# def f1():
#     s = "I Love Navgurukul"
#     def f2():
#        print(s)
#     f2()

# f1() 
def f1():
    s = int(input("enter the number"))
    if s%2==0:
        def f2():
            print("even",s)
    
    f2()

f1() 
