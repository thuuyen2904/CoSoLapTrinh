import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
s=(a+b+c)/2
x=s*(s-a)*(s-b)*(s-c)
dientich=math.sqrt(x)
print('Dien tich=',dientich,sep='')