hoten=input('Ho ten: ')
songaycong=int(input('So ngay cong: '))
dongia=int(input('Don gia ngay cong: '))
phucap=float(input('He so phu cap: '))
tamung=int(input('Tam ung: '))
luong=dongia*songaycong*phucap
thuclinh=luong-tamung
print('Nhan vien ',hoten,',',' Co tien Luong=',round(luong,1),',',' Tam ung=',tamung,' va Thuc linh=',round(thuclinh,1),sep='')