def calculator():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    op=input("enter the oparator")
    if(op=="+"):
        add_result=a+b
        return add_result
    elif(op=="-"):
        substr_result=a-b
        return substr_result
    elif(op=="*"):
        multiply_result=a*b
        return multiply_result
    elif(op=="/"):
        division_result=a/b
        return division_result
    else:
        print("no oparator")
add_result=calculator()
print(add_result)
substr_result=calculator()
print(substr_result)
substr_result=calculator()
print(substr_result)
substr_result=calculator()
print(substr_result)