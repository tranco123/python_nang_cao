# Ngày 2 – Hàm nâng cao:
# Hàm có tham số mặc định, *args, **kwargs
# Hàm lồng nhau, biến toàn cục/cục bộ
#--------------------------------------------
#A-Tham số mặc định :Khi bạn muốn một tham số có giá trị mặc định nếu không truyền vào khi gọi hàm.
# Ví dụ 
# def chao(ten="ban") :
#     print(f"chao {ten}")
# chao()  # Chao ban 
# chao("Linh") #Chao Linh 
# Note : Nhưng mà cái này a thấy thương ít vào , nó ko đa dạng cho lắm 
#------------------------------------------
#B-*arg : truyền vào nhiều đối số mk không biết trước (thường là truyền vào kiểu dạng tuple )
#Ví dụ : 
# def tinhtong(*args) # Chỗ này tại sao lại có dấu '*' : Vì dấu * này sẽ hiểu là mk truyền nhiều đối số vào , nếu ko có dấu * này nó sẽ hiểu mk truyền vào 1 số bất kì 
#     print(args)
#     return sum(args) #Tại sao chỗ này lại ko còn '*' nữa : Ví hàm sum chỉ dạng nhận dạng số như 1,2,3... 
# print(tinhtong(2 ,3 ,4)) 
#------------------------------------------
#C- **kwargs : truyền có nhiều đối số có tên(chủ yếu dạng : key - value)
# Ví dụ : 
# def xem_thong_tin(**kwargs):  # Dấu '**' tức là mình truyền cho nó 1 dạng từ điển có dạng khoá - giá trị thường chủ yếu là vậy 
#     for v,k in kwargs.items(): # items là dạng key - value trong trường hợp này nó sẽ hiểu v là khoá , k là giá trị 
#         print(f"{v} : {k}")
# xem_thong_tin(ten = "Linh", tuoi = 19)
#------------------------------------------
#D - Biến toàn cục(global) và biến cục bộ (local)
# 1- Biến cục bộ(local) :Là biến được khai báo bên trong một hàm, chỉ dùng được trong hàm đó.
#Ví dụ : 
# def tinh_toan():
#     x = 4 # Biến này gọi là biến cục bộ nè 
#     kq = x + 2 
#     return kq
# print(tinh_toan())
# 2- Biến toàn cục(global): Là biến được khai báo có thể sử dung trong hàm hoặc ngoài hàm.
#Ví dụ :
# x = 16 
# def tinh_toan():
#     global x # Tại sao lại có câu lệnh này : Vì khi mk gọi global nó sẽ hiểu cái x kia là biến toàn cục vì nó nằm ngoài hàm def 
#     kq = x + 4 
#     return kq 
# kq = x + 2
# print(kq)
# print(tinh_toan())
#------------------------------------------
#BÀI TẬP THỰC HÀNH 
# Bài 1 : Viết hàm may_tinh() có các chức năng:
# Nhận vào một phép toán ('+','*')
# Nhận nhiều số bằng *args
# Có tham số mặc định là phép cộng nếu không nhập
# Dùng hàm lồng trong hàm để thực hiện tính toán
#Tính toán : 
# def tinh_toan(phep_tinh=' ', *args):
#     def tinh():
#         if phep_tinh == '+':
#             return sum(args)
#         elif phep_tinh == '*':
#             kq = 1 
#             for i in args :
#                 kq *= i 
#             return kq 
#     return tinh()
# print(tinh_toan('*' ,1,2,3,4))
# Bài 2 :Thông tin sinh viên linh hoạt
# Yêu cầu:
# Viết hàm in_thong_tin() nhận bất kỳ thông tin gì về sinh viên: tên, tuổi, lớp, email...
# Dùng **kwargs để nhận dữ liệu linh hoạt
# Trong hàm, in ra mỗi dòng một thông tin
# Biến trường = "UNETI" là biến toàn cục, phải dùng trong hàm

# Mình nghĩ nó đơn giản thui đừng nghĩ khó quá lên : 
truong = "Uneti" 
def xem_thong_tin_sinh_vien(**kwargs):
    global truong 
    print(f"Truong : {truong}")
    for v,k in kwargs.items():
        print(f"{v} :{k}")
    return
xem_thong_tin_sinh_vien(ten = "Linh", lop = "DHKL18A2HN", tuoi = 19, email = "tttl.24174600088@gmail.com")




# Có vấn đề nào em ko hiểu ko ? mấy cái code kia xem phải tụ gõ lại nhá , gõ đến bao giờ mk ko bị vướng chỗ nào thì thôi và hiểu rõ từng vấn đề 
# Chúc gái có 1 ngày vui vẻ hẹ hẹ 