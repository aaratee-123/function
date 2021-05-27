# Ek perfect() naam ka function define kijiye joki ek parameter lega aur uss parameter 
# ko hume check karana hai ki vo perfect number hain ya nahi. 
# Iske baad uss function ko use karke ek program likhiye jo ki 1 se 1000 tak sabhi perfect numbers
#  ko print kare.[ hum ek aise integer number ko perfect number 
#  kahenge jo ki uske sabhi factors ( including 1 & excluding itself) ka sum uss number ke barabar hota hai. Example:- Expected Output :- 

def perfect():
    t=1
    while t<=1000:
        sum=0
        temp=t
        while temp>0:
            i=1
            f=1
            reminder=temp%10
            while i<=reminder:
                f=f*i
                i=i+1
            sum=sum+f
            temp=temp//10
        if sum==t:
            print("it is perfect number",sum)
        t=t+1
perfect()