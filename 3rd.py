li = []
n = int(input("enter the length of the array"))
flag = 0
count = 0
for i in range(n):
    x=int(input("enter the element"+str(i+1)+":"))
    li.append(x)
print("the array elements are",li)
item=int(input("enter  the element to be search"))
for i in li:
    count=count+1
    if(item==i):
        flag=1
        break
if(flag==1):
    print("search is successfull found at",count)
else:
    print("search is unsuccessfull")
