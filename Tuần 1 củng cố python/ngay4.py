#Ngày 4- Làm việc với file 
#Đọc ghi file văn bản , csv 
#Đọc json và ghi json 
#----------------------------------------
#A-Đọc ghi file văn bản , csv 
#1-Ghi file 
# #Cú pháp : 
# with open("Link mà mk copy path",'w',encoding= 'utf -8') as f :
#w : ghi nhớ 
#encoding= 'uft -8' : python sẽ hiểu mk chuyển sang tiếng việt 
#as f : tức là đặt tên cho cái cụm trong ngoặc đó là f 
#2- Đọc file :
#with open("Link mà mk copy path",'r',encoding= 'utf -8') as f :
#r : đọc file (Mẹo làm nhanh đọc file mình chỉ cần copy ghi file bên trên rồi dán xuống dưới, thay 'w' thành 'r')
#----------------------------------------
#2-Đọc ghi file csv 
#1- Ghi file .csv 
#CÚ PHÁP : 
#import csv : # bắt buộc phải có khi dùng file csv 
#du_lieu = [['Ten', 'Tuoi'], ['An', 20], ['Binh', 22]]
#with open('Copy path', 'w',newline='',encoding= 'uft-8' as f :
#    writer = csv.writer(f)    # dùng để ghi từng dòng dữ liệu vào file CSV theo đúng định dạng.
#    writer.writerows(du_lieu) #để ghi nhiều dòng dữ liệu một lần.
#'Newline=" "' :đảm bảo khi ghi ko bị dòng trắng  giữa các dòng
#2- Đọc file .csv 
#CÚ PHÁP 
# import csv
# with open('COPY PATH', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f) #Đọc từng dòng 
#     for dong in reader:
#         print(dong)
#----------------------------------------
#B- JSON : 
#ĐỊNH NGHĨA : JSON là một định dạng dữ liệu : gọn nhẹ, dễ đọc, dễ xử lý 
# Các hàm json : 
#- Ghi file Json            -CÚ PHÁP : json.dump(object,file)
#- Đọc file json            -CÚ PHÁP : json.load(file)
#- Chuyển json ->  chuỗi    -CÚ PHÁP : json.dumps(ôbject)
#- Chuỗi -> object python   -CÚ PHÁP : json.loads(string)
#BÀI TẬP THỰC HÀNH JSON : 
#BÀI 1 : 
#Cho file sinhvien.json như sau : 
# [
#   {"ten": "An", "tuoi": 20, "lop": "DHKH01", "diem": 8.5},
#   {"ten": "Binh", "tuoi": 21, "lop": "DHKH01", "diem": 6.0},
#   {"ten": "Chi", "tuoi": 19, "lop": "DHKH02", "diem": 9.0}
# ]
#a-Hiển thị toàn bộ danh sách sinh viên (Dùng json.load)
#b-Thêm sinh viên mới do người nhập (Dùng json.dump)
#c-Lọc ra sinh viên có điểm trên 8 
#d-Tăng điểm của tất cả sinh viên lớp "DHKH01" lên 0,5 điểm 
#e-Lưu lại dữ liệu sau khi vưa chỉnh sửa 
#ĐÂU TIEN TẠO DANH SÁCH SINH VIÊN JSON 
import json
with open('sinhvienngay4.json','r',encoding='utf-8') as f : 
    ds = json.load(f)
print(ds)
#Them sinh vien 
ten = input("Nhap ten ban can them : ")
tuoi = int(input("Nhap tuoi ban can them: "))
lop = input("Nhap lop cua ban can them: ")
diem = float(input("Nhap diem ban can them: "))
ds.append({
    "ten": ten,
    "tuoi": tuoi,
    "lop": lop,
    "diem": diem
})
print(type(ds))
# Lọc danh sách có điểm trên 8 
for i in ds : 
    if i['diem'] >= 8 : 
        print(i)
for sv in ds: 
    if sv['lop'] == 'DHKH01': 
        sv['diem'] += 0.5
        print(f"Đã tăng điểm cho {sv['ten']} lên {sv['diem']}")

# Ghi lại danh sách sau khi thêm sinh viên
with open('sinhvienngay4.json', 'w', encoding='utf-8') as f:
    json.dump(ds, f, ensure_ascii=False, indent=2)

print("Đã thêm sinh viên và lưu vào file thành công")
