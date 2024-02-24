#break
# s="hello"
# for i in s:
#     if(i=="l"):
#         break
#     print(i)

#continue
# s="hello"
# for i in s:
#     if(i=="l"):
#         continue
#     print(i)

#print upto specified character
s="python is a programming language"
chr=s
for i in s:
    if(i=="chr"):
        break
    print(i)

#skip even numbrs
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     if(i%2==0):
#         continue
#     print(i)

#1500 to 2700 not divisible by 7
# for i in range(1500,2701):
#     if(i%7==0):
#         continue
#
#     print(i)

#pass
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     if(i==2):
#         pass
#     else:
#         print(i)

#
# for i in range(1,4):
#     for j in range(1,4):
#
#         print(i,j)

#
# l=["kelly","jessa","emma"]
# for i in l:
#     for j in l:
#
#           print(i,end=" ")
#     print()

# output
# "kelly","kelly","kelly"
# "jessa","jessa","jessa"
# "emma","emma","emma"



# number=[1,2,3]
# question=["what","when","why"]
# for i in number:
#     print(i)
#     for j in question:
#         print(j)
# output
# 1.
# what
# when
# why
# 2.
# what
# when
# why
# 3.
# what
# when
# why

# l1=[2,4,6]
# l2=[2,4,6]
# for i in l1:
#     for j in l2:
#         print(i+j,end=" ")
#     print()

# output
# 4 6 8
# 6 8 10
# 8 10 12


# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()
#output
#1 2 3 4..10
# 2 4 6.... 20
# 3 6 9....30
#......
#10,20,30...100

# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# 1
# 1,2
# 1,2,3