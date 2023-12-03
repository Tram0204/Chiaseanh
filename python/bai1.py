nam = int(input("Nhập số nguyên n: "))
if ((nam > 1900) and (nam < 2900)): 
    if (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
     print('Nam nhuan')
    else:
     print('Nam khong nhuan')
    
else:
     print('Nhập lại n: ')
     