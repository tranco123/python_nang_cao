#Buổi 5: Xử lý ngoại lệ 
#Try - except -finally 
#------------------------------------------
#A- try-except-finally 
#Cú pháp :
# try : 
#     #Đoạn code có thể lỗi 
# except : 
#     #Bắt lỗi xem mk sai ở vị trí nào 
# finally: 
#     #Dù có lỗi nhưng mà nó vẫn chạy đoạn code tiếp theo 
#Ví dụ 1 : Bắt lỗi ko chia hết cho 2 :
try : 
    n = int(input("Nhập số n mà bạn muốn kiểm tra : "))
    if n % 2 == 0 :
        print("n chia hết cho 2 ")
except ValueError : 
    print("Bạn nhập n sai ")
finally:
    print("Chương trình kết thúc")

#NOTE trong phần except : 
# except valueError        : dùng để kiểm tra lỗi về giá trị
# except ZeroDivisionError : dùng bắt lỗi chia cho 0 
# except FileNotFoundError : dùng bắt lỗi ko tìm thấy file (thường dùng trong đọc và ghi file)
