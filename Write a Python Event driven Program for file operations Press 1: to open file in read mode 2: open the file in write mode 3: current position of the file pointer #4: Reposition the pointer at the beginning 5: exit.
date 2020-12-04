import sys
while(True):
    print(" 1.open the file in write mode \n 2.open the file in read mode \n 3.current position of the file pointer \n 4.reposition the pointer at the beg \n 5.exit")
    op=input("enter your option")
    if(op=='1'):
        file_name=input("enter the file name")
        fo=open(file_name,'w')
        str1=input("enter a string")
        fo.write(str1)
        fo.close()
    if(op=='2'):
        try:
            file_name=input("enter the file name")
            fo=open(file_name,'r')
        except IOError:
            print("the file does not exist")
        else:
            print("name of the file",fo.name)
            print("is the file closed",fo.closed)
            print("opening mode:",fo.mode)
            print("file contents:",fo.read())
            fo.close()
    if(op=='3'):
        try:
            file_name=input("enter the file name")
            fo=open(file_name,"r")
        except IOError:
            print("the file doesn't exist")
        else:
            print("file pointer position before read()",fo.tell())
            print("file contents:",fo.read())
            print("file pointer pos after read()",fo.tell())
            fo.close()
    if(op=='4'):
        try:
            file_name=input("enter name of the file")
            fo=open(file_name,"a")
        except IOError:
            print("The file doesn't exist")
        else:
            print("file pointer pos after open()",fo.tell())
            pos=fo.seek(0,0)
            print("Now file pointer after seek(0,0)",fo.tell())
            str1=input("enter some more contents:")
            fo.write(str1)
            print("Now file pointer after write",fo.tell())
            fo.close()
    if(op=='5'):
        sys.exit()
