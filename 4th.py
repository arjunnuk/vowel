li=[]
flag=0
n=int(input("enter the size of the array"))
for i in range (n):
    x=int(input("enter the element"+str(i+1)+":"))
    li.append(x)
    li.sort()
print("the array elements are",li)
item=int(input("enter the element to be searched"))
low=0
high=n-1
while(low<=high):
    mid=(low+high)//2
    if(item==li[mid]) :
     flag=1
     break
    elif(item<li[mid]):
      high=mid-1
    else:
      low=mid+1
if(flag==1):
        print("search is successful and  found at position",mid+1)
else:
        print("search is unsuccessfull")