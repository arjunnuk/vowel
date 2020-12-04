def push(stack):
    global max_else, top
    if(top>=max_ele-1):
        print("stack is overflow")
    else:
        x=input("enter the element")
        stack.append(x)
        top+=1
        display(stack)
def pop(stack):
    global top
    if(top==-1):
        print("stack is underflow")
    else:
        print("stack before popping")
        display(stack)
        print("the popped element is",stack.pop())
        top-=1
        print("stack after popping")
        display(stack)
def display (stack):
    if(top==-1):
        print("the stack is empty \n \n")
    else:
        print("the elements of stack \n")
        print("----------------------\n",stack)
def default (stack):
    exit()
def main():
    ch=0
    stack=[]
    global max_ele
    max_ele=int(input("enter the length of the stack"))
    menu={"1":push,"2":pop,"3":display,"4":default}
    while(ch!=4):
        print("\n menu \n1.push \n2.pop \n3.display \n4.exit \n")
        ch=input("enter your choice")
        menu.get(ch) (stack)
top=-1
max_ele=0
main()
