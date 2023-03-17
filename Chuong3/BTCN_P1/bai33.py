x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')
if ch=="+":
    a=x+y
    print(x,ch,y,'=',round(a,1),sep='')
elif ch=='-':
    a=x-y
    print(x,ch,y,'=',round(a,1),sep='')
elif ch=='*':
    a=x*y
    print(x,ch,y,'=',round(a,1),sep='')
elif ch=='/':
    if y==0:
        print('Khong hop le')
    else:
        a=x/y
        print(x,ch,y,'=',round(a,1),sep='')
else:
    print('Khong hop le')
    
    