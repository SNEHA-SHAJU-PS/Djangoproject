#write accessmode
#f=open("k.txt",'w')
# f.write("hello")
# f.write("python\n")
# f.write("language")
# f.close()

#read accessmode
#f=open("k.txt","r")
# f.read()
# print(f.read())
# f.close()

#append accessmode
# append the content of one text file into another file.and display the content
# f=open('p.txt','r')
# s=f.read()
# g=open('k.txt','a')
# g.write(s)
# g.close()
# f=open('k.txt','a')
# print(f.read())

#f=open("p.txt","w")
#
#append the content of one txt file into another file.and disply content
# f=open('p.txt','r')
# s=f.read()
# g=open('k.txt','a')
# g.write(s)
# g.close()
# f=open('k.txt','r')
# print(f.read())


# find the no of lines in a file
# f=open('k.txt','r')
# print(len(f.readlines()))
#
#
# search a particular word in a file
# f=open('k.txt','r')
# s=f.read()
# print(s)
# if 'hello'in s:
#     print('word found')
# else:
#     print('word not found')


# find no of uppercase lowercase spaces digits in a file
# c1=0
# c2=0
# c3=0
# c4=0
# f=open('k.txt','r')
# s=f.read()
# for i in s:
#     if(i.isspace()):
#         c1=c1+1
#     elif(i.isdigit()):
#         c2=c2+1
#     elif(i.isupper()):
#         c3=c3+1
#     elif(i.islower()):
#         c4=c4+1
# print('space',c1,'digit',c2,'upper',c3,'lower',c4)

#menu driven code
def file_create():
    filename=input("enter the filename")
    f=open(filename,"w")
    content=input("enter the content")
    f.write(content)
    f.close()

def file_read():
    try:#exception handling
         filename = input("enter the filename")
         f = open(filename,"r")
         print(f.read())
    except:#exception handling
        print("file is not found")
    else:
        pass

def file_append():
    filename = input("enter the filename")
    f = open(filename,"a+")
    content = input("enter the content")
    f.write(content)
    f.seek(0,0)
    print(f.read())

def file_search():
    filename = input("enter the filename")
    f = open(filename,"r")
    s=f.read()
    word= input("enter the word")
    if word in s:
        print("word is found")
    else:
        print("word is not found")

def file_remove():
    try:
         filename=input("enter the filename")
         import os
         os.remove(filename)
         print("file is deleted")
    except:
        print("file is not found")
    else:
        pass

while(1):
    print('1.file create')
    print('2.file read')
    print('3.file append')
    print('4.file search')
    print('5.file remove')
    print('6.exit')
    ch=int(input("enter your choice"))
    if ch==1:
        file_create()
    elif ch==2:
        file_read()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_remove()
    else:
        exit( )










