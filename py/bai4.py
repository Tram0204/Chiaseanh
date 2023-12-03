namKhongNhuan = [31,28,31,30,31,30,31,31,30,31,30,31]
namNhuan = [31,29,31,30,31,30,31,31,30,31,30,31]
tongNgay=0
day = int(input("Ngày: "))
month = int(input("Tháng: "))
year= int(input("Năm: "))
if(month == 1):
                tongNgay = day
elif (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            for i in range(0,month-1):
                tongNgay = int(tongNgay+namNhuan[i])   
            tongNgay = tongNgay + day
else:
            for i in range(0,month-1):
                tongNgay = int(tongNgay+namKhongNhuan[i])
            tongNgay = tongNgay + day
print("Tổng ngày từ đầu năm tới hiện thời: {0}".format(tongNgay))