# calculator naam ka ek function banao jo teen argument leta ho -
#  number_x, number_y, operation. number_x aur number_y 
# mein hum humesha do integers denge aur operation mein kaunsa operation karna hai woh denge.
#  Jaise: * Agar operation mein "add" diya toh number_x aur number_y ko add kar ke returna karega.
def calculator (number_x,number_y,operation):
    add=number_x+number_y
    subtract=number_x-number_y
    multiply=number_x*number_y
    divide=number_x/number_y
    return add
#addition=calculator(20,25,"add")
# substraction=calculator(40, 3, "subtract") 
# multiplication=calculator(10, 4, "multiply")
# division=calculator(40, 4, "divide") 
#print(addition)
number_1=calculator(24,20,"add")
print(number_1)
number_2=calculator(50,60,"multiply")
print(number_2)
number_3=calculator(80,120,"divide")
print(number_3)
number_4=calculator(90,23,"substract")
print(number_4)

