m1=int(input('M1='))
m2=int(input('M2='))
m3=int(input('M3='))
s=int(input('S='))
if 1<=s<=100:
    phaitra=s*m1
elif s<=150:
    phaitra=m1*100+m2*(s-100)
else:
    phaitra=m1*100+m2*50+m3*(s-150)
print('Phai tra=',phaitra,sep='')