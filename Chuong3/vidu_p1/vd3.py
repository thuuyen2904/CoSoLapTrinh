yos=int(input('yrsOfService = '))
b=int(input('salary = '))
bonus=int(input('bonus = '))

    
# if yos < 5 :
#     if b < 500 :
#         bonus = 100
#     esle:  
#         bonus = 2
# else:
#     bonus = 700
# print('Bonus amount: ',bonus)  
# if yos<5:
#     if b < 500 :
#         bonus = 600 
#     else: 
#         bonus = 6504
# else:
#     bonus =700
if yos < 5:
    if b< 500:
        bonus = 100
    else:
        bonus = 200
else:
    bonus = 700
print('Bonus amount: ',bonus)  