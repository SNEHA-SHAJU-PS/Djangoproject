#1)match
# matched---->
# import re
# s="pet:cat I love cats"
# m=re.match(r'pet:\w\w\w',s)
# if(m):
#     print("match found")
#     print(m.group())
# else:
#     print('match not found')

#umatched--->
# import re
# s=" I love cats pet:cats"
# m=re.match(r'pet:\w\w\w',s)
# if(m):
#     print("match found")
# else:
#     print('match not found')

# 2) search
# import re
# s=" I love cats pet:cats"
# m=re.search(r'pet:\w\w\w',s)
# if(m):
#     print("match found")
#
# else:
#     print('match not found')

#findall
# import re
# s=" I love cats pet:cats i love pet:cow"
#
# m=re.findall(r'pet:\w\w\w',s)
# if(m):
#     print("match found")
#     print(m)
# else:
#     print('match not found')

#Q
#import re
# s='mat cat rat bat sat pat'
# #starting with s,pr ends at
# m=re.findall(r'[spr]at',s)
# if(m):
#     print("match found")
#     print(m)
# else:
#     print("not match")

#Q
#except s,p,r ends at
# import re
# s='mat cat rat bat sat pat'
# #starting with s,pr ends at
# m=re.findall(r'[^spr]at',s)
# if(m):
#     print("match found")
#     print(m)
# else:
#     print("not match")

#Q
# write a pgm(wap) to extract yr month date from a url
# url="hhttps//www.washingpost.com/news/football-inside/wp/2016/09/02"
# import re
# m=re.search(r'\d{4}/\d{2}/\d{2}',url)
# if m:
#     print("match found")
#     print(m.group())
# else:
#     print("not found")

#
#Q wap to find all wrds continig leteer z
# s="abcd abczd zahgd  hdghhjj bhgzh hjsukkz"
# import re
# l=re.findall(r'\b[a-z]*z[a-z]*\b',s)
# print(l)

#
# Q wap to check wheather a string contains only upper,lower case,digit,and symnbol
# s="ddff555_gklllll"
# import re
# l=re.search(r'^\w+$',s)#upper lower digits underscore
#
# if l:
#     print("match found")
# else:
#     print("mot fund")
#
#Q wap to replaxce all occurence space.comma.or dot with colon
s="python is pgm, g languge."
import re
m=re.sub(r'[, .]',":",s)
print(m)


