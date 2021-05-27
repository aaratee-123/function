# add_numbers_list naam ka function likhiye jo do integers ki 2 lists leta ho aur fir same
#  position wale integers ka sum print karta ho.Same position waale 2 integers ka sum karne 
#  ke liye Part 1 meindi gayi add_numbers waale function ka use karo.
#   Jaise agar hum iss function ko [50, 60, 10] aur [10, 20, 13] denge ko woh yeh print karega

def add_number_list():
    i=0
    list1=[50,60,10]
    list2=[10,20,13]
    s=0
    while i<len(list1):
        s=list1[i]+list2[i]
        i=i+1
        print(s)
add_number_list()