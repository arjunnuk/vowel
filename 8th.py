import math
a=float(input("enter the value of a="))
b=float(input("enter the value of b="))
c=float(input("enter the value of c="))
d=b**2-4*a*c
if d<0:
    print("this equation has no real solution")
elif d==0:
  x=(-b+math.sqrt(d))//2*a
  print("this equation has one solution:",x)
else:
    x1=(-b+math.sqrt(d))//2*a
    x2=(-b-math.sqrt(d))//2*a
    print("this equation has two solutions:",x1,"and",x2)