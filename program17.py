# Apko students naam ka ek function define karna hai 
# or uss function mai list of students name 
# as a parameter pass karna hai(List ka use nahi karna hai)


# def student(*list_of_student_name):
#     print(list_of_student_name)
# student("arti","kirti","priti","priya","siya")

def student(name):
    i=0
    a=[]
    while i<5:
        b=input("enter the name")
        a.append(b)
        i=i+1
    print(a)
student("name")


