d={101:{'name':'arun','age':23,'place':'kkm'},
   102:{'name':'hari','age':25},
   103:{'name':'ki','age':23}}
a=d[101]['age']
b=d[102]['age']
c=d[103]['age']
avg=(a+b+c)/3
print('avgerage',avg)

e={101:['arun',23],102:['hi',56]}
a=e[101][1]
b=e[102][1]
avg=(a+b)/2
print('average',avg)
