namnhuan ={"1":"31","2":"29","3":"31","4":"30","5":"31","6":"30","7":"31","8":"31","9":"30","10":"31","11":"30","12":"31",} 
namkhongnhuan ={"1":"31","2":"28","3":"31","4":"30","5":"31","6":"30","7":"31","8":"31","9":"30","10":"31","11":"30","12":"31",}
day = int(input('Nhập vào ngày:'))
month = int(input('Nhập vào tháng:'))
year = int(input('Nhập vào năm:'))
if (year <1980 or year >2900): 
    print("Định dạng năm không hợp lệ !") 
    if (month <=0 or month >12): 
        print("Định dạng tháng không hợp lệ") 
    if(day <=0 or day>31): 
            print("Định dạng ngày không hợp lệ") 
    if (year% 400 == 0) or (year% 4 == 0 and year % 100 != 0 ): 
        if (day<= int (namnhuan[str (month)])): 
                print("Định dạng ngày hợp lệ") 
        else: 
                print("Định dạng ngày không hợp lệ")
else:              
    if (day <= int (namkhongnhuan[str (month)])): 
                    print("Định dạng ngày hợp lệ") 
    else: 
                    print("Định dạng ngày không hợp lệ")