# # Ngày 1 – Củng cố kiến thức nền tảng:
# # Kiểu dữ liệu nâng cao: set, dict, tuple
# # Ôn list comprehension, unpacking
# #A.Tuple - Bộ giá trị không thay đổi- Là tập hợp có thứ tự, bất biến(không thể sửa khi tạo)
# #- Dùng khi bạn muốn dữ liệu không thể thay đổi 
# #- Dùng tuple khi dữ liệu cố định như toạ độ , ngày tháng ... 
# eg = (1,2,3) 
# print(eg[1]) #output = 2 
# eg[2]= 3 # thay đổi số trong tuple 
# print(eg) # Báo lỗi không thay đổi được 
#------------------------------------------------------
# #B.Set- Tập hợp không trùng lặp"-không chứa phần tử trùng nhau";"Không có kí tự , không có chỉ số index"
# tap_hop = {1,2,3,4,5,6}
# print(tap_hop)
# # Phép toán thông dụng thường dùng 
# a = {1,2,3}
# b = {1,2,4,5,6}
# print(a & b ) # Phép giao 
# print(a|b) # Phép hợp 
# print(a-b) # Phép hiệu 
#-----------------------------------------------------
#C-Dictionary(Dict) - Chứa bộ giá trị gồm key:valune (dạng tự điễn bắt buộc phải có {})
# sinhvien = {"ten":"Co","tuoi": 19 }
# print(sinhvien["ten"])
# print(sinhvien["tuoi"])
#-----------------------------------------------------
#D. List Comprehension – Viết danh sách gọn gàng
# Ví dụ: tạo 1 danh sách tìm số chẵn trong đó 
# Cách làm bình thường :
# so_chan = []
# for i in range(11):
#     if i % 2 ==0 :
#         so_chan.append(i)
# print(so_chan)
#Sau khi viết lại : 
# so_chan = [i for i in range(11) if i % 2 == 0 ]
# print(so_chan)
#-----------------------------------------------------
#BÀI TẬP THỰC HÀNH : 
#Bài 1 : Yêu cầu: Nhập vào một chuỗi, in ra số lần xuất hiện của từng ký tự (dùng dict).
# Ví dụ :
# Nhập: "lap trinh"
# Kết quả: {'l': 1, 'a': 1, 'p': 1, ' ': 1, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'h': 1}
# nhap_chuoi_cua_ban = input("Nhap chuoi ban : ")
# dem_ki_tu = {}
# for ki_tu in nhap_chuoi_cua_ban:
#     if ki_tu in dem_ki_tu:
#         dem_ki_tu[ki_tu] += 1 
#     else :
#         dem_ki_tu[ki_tu] = 1 
# print("Ket qua cua ban la : ")
# for k,v in dem_ki_tu.items():   #items() : Mục đích là trả về dict "key : value"
#     print(f"{k}:So lan lap lai cua chuoi la {v}")
#Bài 2 :Loại bỏ số trùng và đếm số lẻ
nhap_so = input(f"Nhap day so cua ban :")
ds_so = list(map(int, nhap_so.split()))
tinh_toan = set(ds_so)
dem_le = 0 
for i in tinh_toan:
    if i % 2 !=  0 :
        dem_le+= 1 
print(dem_le)
