li=[]
n=int(input("enter the number of elements"))
for i in range(n):
    x=int(input("enter the elements"))
    li.append(x)
li.sort()
print("the sorted array is \n",li)
item=int(input("enter the element to be inserted"))
count,flag=0,0
for i in li:
    if(i>item):
        li.insert(count,item)
        flag=1
        break
    count+=1
if(flag==0):
    li.insert(count,item)
print("the array after inserting the element is \n",li)
