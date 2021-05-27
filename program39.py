# list_change naam ka ek function ka code likho jo 2 lists 
# jisme integers arguments ki tarah le aur fir unn lists ki woh items 
# jo same index number (kram) pe hain unko multiply kar ke ek nayi list return karvaye.
#  Aapko multiply karne ke liye calculator function ka use karna hai. Normal tareeke se
#   multiply nahi kar sakte ho. Jaise agar hum function ko aise call karenge toh:
 
# multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5]) 

# Yahan multiple_list ki yeh value honi chaiye:
 
# [10, 200, 150, 100] 

# 10, 5 aur 2 ko multiple kar ke aaya, 200 10 aur 20 ko multiple kar ke, 150 50 aur 3 ko, 
# # 100 20 aur 5 ko.
# def list_change(list1,list2):
#     i=0
#     while i<len(list1):
#         j=0
#         while j<len(list2):
#             if list[i]==list[j]:
#                 list=list[i]*list[j]
#                 print(list)
# multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])


# 100 20 aur 5 ko.
def list_change(list1,list2):
    i=0
    y=[]
    while i<len(list1):
        j=0
        while j<len(list2):
                k= list1[i]*list2[j]
                y.append(k)
                j=j+1
                i=i+1
    print(y)
list_change([5, 10, 50, 20], [2, 20, 3, 5]) 


