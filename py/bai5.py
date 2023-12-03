
import os
import random
namKhongNhuan = [31,28,31,30,31,30,31,31,30,31,30,31]
namNhuan = [31,29,31,30,31,30,31,31,30,31,30,31]
while(True):
    print("\n\n\t========MENU=========\n\n")
    print("Bai 4: Tính tổng số ngày từ 1/1 tới hiện thời")
    print("Bài 5: Tìm kho báu\n")
    print("Kết thúc bài : 0\n\n")
    luachon = int(input("Nhập lựa chọn của bạn: "))
    if(luachon==4):
        os.system("cls")
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
        os.system("pause")
    elif(luachon == 5):
        os.system("cls")
        canhcua =["Win","Lose","Die"]
        random.shuffle(canhcua)
        print("\n\nCánh Cửa 1", end="\t\t");print("Cánh Cửa 2",end="\t\t");print("Cánh Cửa 3",end="\t\t")
        print("\n\n\n")
        while(True):
            
            canhcuamayman = int(input("Vui lòng nhập cánh cửa bạn mong muốn: "))
            if(canhcuamayman>0 and canhcuamayman<3):
                break
            else:
                os.system("cls")
                print("Cánh cửa bạn chọn không tồn tại vui lòng nhập lại !\n\n")
                os.system("pause")
        if(canhcuamayman == 1):
            os.system("cls")
            if(canhcua[0]=="Win"):
                print("\n\n")
                print("\t\t"+canhcua[0],end="\t\t");print("\t\t"+canhcua[1],end="\t\t");print("\t\t"+canhcua[2],end="\t\t")
                print("\n\n\n\n\t\t\tChúc mừng bạn nhận được khó báu và chiến thắng !\n\n")
                os.system("pause")
            elif(canhcua[0]=="Lose"):
                print("\n\n")
                print("\t\t"+canhcua[0],end="\t\t");print("\t\t"+canhcua[1],end="\t\t");print("\t\t"+canhcua[2],end="\t\t")
                print("\n\n\n\n\t\t\tÔi không bạn đã gặp phải quái vật !\n\n")
                os.system("pause")
            else:
                print("\n\n")
                print("\t\t"+canhcua[0],end="\t\t");print("\t\t"+canhcua[1],end="\t\t");print("\t\t"+canhcua[2],end="\t\t")
                print("\n\n\n\n\t\t\t\t\tYour Die !\n\n")
                os.system("pause")
        if(canhcuamayman == 2):
            os.system("cls")
            if(canhcua[1]=="Win"):
                print("\n\n")
                print("\t\t"+canhcua[0],end="\t\t");print("\t\t"+canhcua[1],end="\t\t");print("\t\t"+canhcua[2],end="\t\t")
                print("\n\n\n\n\t\t\tChúc mừng bạn nhận được khó báu và chiến thắng !\n\n")
                os.system("pause")
            elif(canhcua[1]=="Lose"):
                print("\n\n")
                print("\t\t"+canhcua[0],end="\t\t");print("\t\t"+canhcua[1],end="\t\t");print("\t\t"+canhcua[2],end="\t\t")
                print("\n\n\n\n\t\t\tÔi không bạn đã gặp phải quái vật !\n\n")
                os.system("pause")
            elif(canhcua[1]=="Die"):
                print("\n\n")
                print("\t\t"+canhcua[0],end="\t\t");print("\t\t"+canhcua[1],end="\t\t");print("\t\t"+canhcua[2],end="\t\t")
                print("\n\n\n\n\t\t\t\t\tYour Die !\n\n")
                os.system("pause")
        if(canhcuamayman == 3):
            os.system("cls")
            if(canhcua[2]=="Win"):
                print("\n\n")
                print("\t\t"+canhcua[0],end="\t\t");print("\t\t"+canhcua[1],end="\t\t");print("\t\t"+canhcua[2],end="\t\t")
                print("\n\n\n\n\t\t\tChúc mừng bạn nhận được khó báu và chiến thắng !\n\n")
                os.system("pause")
            elif(canhcua[2]=="Lose"):
                print("\n\n")
                print("\t\t"+canhcua[0],end="\t\t");print("\t\t"+canhcua[1],end="\t\t");print("\t\t"+canhcua[2],end="\t\t")
                print("\n\n\n\n\t\t\tÔi không bạn đã gặp phải quái vật !\n\n")
                os.system("pause")
            elif(canhcua[2]=="Die"):
                print("\n\n")
                print("\t\t"+canhcua[0],end="\t\t");print("\t\t"+canhcua[1],end="\t\t");print("\t\t"+canhcua[2],end="\t\t")
                print("\n\n\n\n\t\t\t\tYour Die !\n\n")
                os.system("pause")
    elif(luachon ==0):
        break
