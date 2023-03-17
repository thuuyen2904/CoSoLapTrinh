tieuthu=int(input('Tieu thu='))
if 1<=tieuthu<=100:
    a=550*tieuthu
elif tieuthu<=150:
    a=550*100+(tieuthu-100)*750
elif tieuthu<=200:
    a=550*100+750*50+(tieuthu-150)*950
else:
    a=550*100+750*50+50*950+1350*(tieuthu-200)
thanhtien=a+a*0.1 
print('Phai tra=',thanhtien,sep='')   