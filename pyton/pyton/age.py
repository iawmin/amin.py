import math
a=int(input("what year is it today?  "))
b=int(input("what month is it today?  "))
c=int(input("what time is it? "))
d=int(input("what year were you born? "))
e=int(input("what month were you born? "))
f=int(input("what day were you? "))
j=(a-d)-1, 12-(e-b) , 30-(c-f)   
h=(a-d), (b-e), (c-f)
i=(a-d)-1, 11-(e-b), (30-(f-c))
x=(a-d),(b-e)-1,30-(f-c)
if e>=b and c>=f:
    print(j)
elif b>=e and c>=f:
    print(h)
elif e>=b and f>=c:
    print(i)
else:
    print(x)
year=int(input("how year? "))
month=int(input("how month? "))
day=int(input("hoe day? "))  
print((year*12*30*24*60*60)+(month*30*24*60*60)+(day*24*60*60))
