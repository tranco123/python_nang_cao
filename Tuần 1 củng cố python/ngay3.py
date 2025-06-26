#Ngày 3 :Đệ quy và lamda 
#-------------------------------------
#A-Đệ quy :là hàm gọi lại chính nó để giải quyết bài toán nhỏ hơn 
#Ví dụ :Tính giai thừa bằng đệ quy : 
def giai_thua(n): 
    if n == 1 or n == 0 : 
        return 1 
    return giai_thua(n -1) * n 
print(giai_thua(5)) #out : 120 
#-------------------------------------
#B-Lambda và các hàm bậc cao : 
#1-Lambda : là 1 cách viết hàm rút gọn , ko cần định nghĩa bằng hàm def.("Hay còn gọi hàm ẩn danh, ko cần đặt tên cho nó")
#CÚ PHÁP : lambda biểu thức đầu vào: biểu thức 
#Ví dụ 1 : 
f = lambda x : x + 3 
print(f(4)) # Output = 7 
# Hàm lambda vi du trên sẽ tương đương với hàm def này : 
def tinh(n) : 
    return n + 3 
print(tinh(4))
#Ví dụ 2 : 
f = lambda x, y, z : x + y + z 
print(f(1,2,3)) #output = 6 
#2- Hàm map(): Áp dụng một hàm cho toàn bộ phần tử của danh sách.
#CÚ PHÁP : map(hàm xử lý, danh sách)
#Ví dụ : 
ds = [1,2,3,4,5]
f = list(map(lambda x : x**2, ds)) # Vì sao cần list trong này ? Vì nếu ko có list, python nó sẽ ko tìm thấy cái ds mà mình tạo bên trên 
print(f)
#3- Hàm filter : Lọc dữ liệu theo điều kiện các phần tử trong danh sách 
#CÚ PHÁP : filter(hàm xử lý, danh sách)
#Ví dụ :
ds = [1,2,3,4,5,6,7] 
f = list(filter(lambda x : x % 2 == 0 , ds))
print(f) #Output = [2,4,6]
#4- Hàm Reduce() : rút gọn danh sách thanh 1 giá trị. 
#CÚ PHÁP :
#from functools import reduce 
#reduce(hàm xử lý, danh sách)
#Ví dụ : 
from functools import reduce # nếu ko có câu này thì mình sẽ gọi được reduce ra 
ds = [2,4,1,3]
f = reduce(lambda x, y : x + y,ds)
print(f)
# Cách chạy thuật toán này là : 
# 2 + 4 = 6 
# 6 +1 = 7 
# 7 + 3 = 10 
# => output = 10 
#NOTE : Sự khác nhau giữa map, filter, reduce 
#- Map thì chỉ tính toán được các phần tử trong danh sách , nếu mà lọc điều kiện trường hợp map này nó trả về true , false ("Ko tin e cứ thử cho hiểu")
#- Filter thì nó sẽ lọc điều trong danh sách đó 
#- Reduce : thường sẽ tính toán toàn bộ danh sách đó rồi đưa 1 kết quả ko lan man dài dòng như 2 cái trên 
#-------------------------------------
#BÀI TẬP THỰC HÀNH : 
# Bài 1 : cho ds = [1, 5, 2, 8, 3, 10, 4]
# -Dùng filter() để lấy các số chẵn và > 3
# -Dùng map() để bình phương các số vừa lọc
# -Dùng reduce() để tính tổng các số bình phương đó
ds = [1,5,2,8,3,10,4]
from functools import reduce 
f = list(filter(lambda x : x % 2 == 0 and  x > 3, ds))
print(f"Kết quả lấy các số chẵn vad lớn hơn 3 : {f}")
L = list(map(lambda x : x ** 2,ds))
print(f"Bình phương các số trong danh sách là : {L}")
C = reduce(lambda x, y : x + y , L)
print(f"Tính tổng tất cả số bình phương trong danh sách : {C}")
#Bài 2 :Cho sv = [('Nam', 7.5), ('Tú', 4.0), ('An', 8.0), ('Linh', 9.2), ('Mai', 5.5)]:
# 1.Lọc ra những sinh viên có điểm >= 5.0 (đạt)
# 2.Dùng map() để tạo danh sách mới gồm chuỗi: "Họ tên: XX, Điểm: YY"
# 3.Dùng reduce() để tính tổng điểm của sinh viên đạt
sv = [('Nam', 7.5), ('Tú', 4.0), ('An', 8.0), ('Linh', 9.2), ('Mai', 5.5),('Co',4)]
loc_ds = list(filter(lambda x : x[1] >= 5,sv))
print(f"Lọc sinh viên có điểm trên trung bình là : {loc_ds}")
ds = list(map(lambda x: f"Ho ten :{x[0]},Diem :{x[1]}",sv))
print(ds)
from functools import reduce 
tinh_tong = reduce(lambda x, y : x + y[1], sv,0) # Tại sao có số 0 ở cuối ? Vì reduce này nó mặc định tính tổng các số chứ ko phải là chữ , vì vậy để số 0 ở cuối để hiểu x ban đầu sẽ là 0 
print(tinh_tong)
