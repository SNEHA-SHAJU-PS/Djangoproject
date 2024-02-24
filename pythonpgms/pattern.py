# for i in range(1,5):
#     for j in range(1,i+1):
#          print('*',end=" ")
#     print()

# output
# *
# * *
# * * *
# * * * *

# 1
# 1 4
# 1 4 9
# 1 4 9 16

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j**2,end=" ")
#     print()

# * * * *
# * * *
# * *
# *

# for i in range(5,-1,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# or
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# 1
# 2 1
# 3 2 1
# 4 3 2 1

# for i in range(1,5):
#     m=i
#     for i in range(1,i+1):
#         print(m,end=" ")
#         m=m-1
#     print()

#OR

# for i in range(1,5):
#
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10

# k=1
# for i in range(1,5):
#
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
# print()

#1

#123

#12345

# for i in range(1,6,2):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()






# 1
#
# 1 2
#
# 1 2 1
#
# 1 2 1 2


# for i in range(1,5):
#     for j in range(1,i+1):
#           if(j%2==0):
#               print(2,end=" ")
#           else:
#               print(1,end=" ")
#     print()


# *
# **
# ***
# ****
# ***
# **
# *
#
#
# n=4
#
# for i in range(1,n+1):
#
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#
# for i in range(3,0,-1):
#
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()


# ****
# ***
# **
# *
# **
# ***
# ****

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# for i in range(1,5):
#     for j in range(1,i+1):
#          print('*',end=" ")
#     print()
#
#
# A
# BB
# CCC
# DDDD

# k=65
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k=k+1
#     print()

# spacing pattern
#    *
#   **
#  ***
# ****

# n=4
# k=6
# for i in range(1,n+1):
#     for p in range(1,k+1):
#         print(end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

#    *
#   **
#  ***
# ****
#  ***
#   **
#    *

# n=4
# k=6
# for i in range(1,n+1):
#     for p in range(1,k+1):
#         print(end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     k=k+2
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#
# **
# ****
# ******
# ********

#
# for i in range(2,10,2):
#      for j in range(1,i+1):
#          print('*',end=" ")
#      print()
#
#            **
#            **
#           ****
#           ****
#          ******
#          ******
#         ********
#         ********
# k=6
# for i in range(2,10,2):
#     for k in range(2):
#         for p in range(1,k+1):
#             print(end=" ")
#         k=k-2
#
#         for j in range(1,i+1):
#             print('*',end=" ")
#         print()

#write a program to print all prime numbers in the range(1,100)


#question
# d={'c1':'india','c2':'bangladesh','c3':'iceland','c4':'newsland','c5':'myanmar'}
#print the country names contsining the word 'land'

# for i in d.values():
#     if('land' in i):
#         print(i)
#or
# for i in d:
#     if('land' in d[i]):
#         print(d[i])

# d=[
#     {'name':'abc',"languages":'a','population':500},
#     {'name':'pqr',"languages":'b','population':300},
#     {'name':'stu',"languages":'c','population':700},
# ]
# #sum of population-->1500(output)
# sum=0
# for i in d:
#     sum=sum+i['population']
# print(sum)





