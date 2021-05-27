# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" 
# agar dono numbers even (2 se divide hote hain) nahi toh
#  print kare "Dono numbers even nahi hai"

def cheak_numbers(a,b):
    if a%2==0 and b%2==0:
        print("dono even hain")
    else:
        print("dono numbers even nahi hai")
cheak_numbers(20,30)
