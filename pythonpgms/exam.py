# d="python"
# for i in range(0,6):
#     for j in range(0,i+1):
#         print(d[j],end=" ")
#     print()
# p
# p y
# p y t
# p y t h
# p y t h o
# p y t h o n

#print the count of vowels in a   string

string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:",vowels)
