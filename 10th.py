s=input("enter a string")
s.lower()
str_rev=s[::-1]
if(s==str_rev):
    print("given string is a palindrome")
else:
    print("not a palindrome")
