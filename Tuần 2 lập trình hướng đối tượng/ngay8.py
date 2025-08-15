#Buổi 8- Lý thuyết OOP 
#Class ; object ; _init_ thuộc tính và phương thức 
#OOP : lập trình hướng đối tượng : 
#--------------------------------------------------------
#A- LỚP VÀ ĐỐI TƯỢNG : 

#1-Lớp (class):
#A- CÁCH KHAI BÁO: 
#Khai báo bắt đầu bằng từ khoá class sau đó tên lớp và dấu hai chấm (:).
#CÚ PHÁP : 
# class className :
    #Khai báo thuộc tính lớp 
    #Khai báo thuộc tinh đối tượng 
    #Khai báo phương thức 
#Ví dụ 1.2.1.1(SGK/5) : Tạo lớp Nhan_vien có chứa id; name; age(3 cái này được gọi là thuộc tính).Lớp này chứa hàm display() đê hiển thị thông tin sinh viên : 
class Nhan_vien :
    id = 16022006 
    name = "Tran thi thuy linh"
    age = 40 
    def display(self): #Trong lớp này tạo ra 1 hàm thì cái này được gọi là : PHƯƠNG THỨC 
                       #display : gọi là tên PHƯƠNG THỨC
                       #self : gọi là THAM CHIẾU
        print(self.id, self.name, self.age)
nv1 = Nhan_vien()
nv1.display() #output = 16022006 Tran thi thuy linh 40
#--------------------------------------------------------
#B- PHƯƠNG THỨC

#- Định nghĩa : phương thức là tập hợp các lệnh python dùng để thực hiện một cách chọn vẹn nhiệm vụ nào đó.
#- Để tạo ra một phương thức mới, ta sử sử dụng khoá "def"
#CÚ PHÁP :
# def MethodName(self,<các tham số khác>):
#     #Các câu lệnh phương thức 

#Ví dụ 1.2.1.2(SGK/7): Tạo lớp DOg với thuộc tính :name, size,age,color và các phương thức : Go,Stay,Lie,Bark,Eat
class Dog :
    Dogcout = 0 # Cái này gọi là biến dùng chung cho tất cả các đối tượng (Đố bt cái này nó có tác dụng j trong đoạn code không ?)
    def __init__(self,name,size,age,color): #self ở đây gọi lại tham chiếu đến chính đối tượng hiện tại : 
        self.name = name  #Tham chiếu đối tượng : ở đây gọi là  tham chiếu tên
        self.size = size 
        self.age = age
        self.color = color 
    def Go(self) : 
        print("I am going run ")
    def Stay(self, place): #Cái palce địa điểm 
        print("I am staying at {} ".format(place)) #fromat này là sẽ truyền vào trong ngoặc nhọn 
    def Lie(self, place):
        print("I am lying at {} ".format(place))
    def BarK(self):
        print("Whoop ...")
    def Eat(self, food):
         print("I am eating at {} ".format(food)) #fromat này cũng là truyền vào trong ngoặc nhọn kia 

bull = Dog("Bull","large", 2, "Yellow") # đặt tên lớp Dog trên là bull và truyền vào nó các tham chiếu đối tượng như là : Name : bull; size :rộng ...
bull.Stay("garden") #gọi hàm def Stay truyền vào fomat là graden 
bull.BarK() 

# - Constructor trong python 
# Giả sử trong tình huống có cần khai báo 1000 nhân viên với thuộc tính : tên; tuổi; công việc thì mk sẽ mất 3000 dònng để khai báo.Vì thế nên ta xây dưng 1 hàm constructor.
# - Vì thế trong python constructor dùng để khới tạo các thể hiện của lớp .Constructor phân làm 2 loại : 
# + Constructor tham số 
# + Constructor không có tham số 
# - Cách Tạo constructor trong python : 
# def _init_(self,<Các tham số khác truyền vào>)              (đặc điểm nhận dạng constructor là luôn có tên "_init_";) 

#VÍ DỤ 1.2.1.3(sgk/8)- Constructor không tham số 
class Dog : 
    def __init__(self):
        print("DAY LA Constructor khong co tham so")
    def display(self, name):
        print('hello',name)

lu = Dog()
lu.display("LU") #output : hello LU   #(output này có thiếu j ko nhỉ ?)

#VÍ DỤ 1.2.1.4(sgk/8): constructor có tham số 
class Dog : 
    def __init__(self,name):
        print("Constructor co tham so")
        self.name = name
    def display(self):
        print("Hello", self.name)

lu = Dog("lu ngoc")
lu.display()
#output : Constructor co tham so
        # Hello lu ngoc
# KHÁC NHAU Constructor GIỮA CÓ THAM SỐ VÀ KHÔNG CÓ THAM SỐ ? (........)

#VÍ DỤ 1.2.1.5(sgk/9) CODE HOÀN CHỈNH:
class Dog : 
    Dogcout = 0 
    def __init__(self,name,age,color,size):
        self.name = name
        self.age = age 
        self.color = color
        self.size = size
    def Go(self):
        print("I am going ...") 
    def Stay(self,place) :
        print("I am staying at {}".format(place))
    def lie(self,place):
        print("I am lying at {}".format(place))
    def Brank(self):
        print("Whoop ...")
    def Eat(self, place):
        print("I am eating at {}".format(place))
bull = Dog("BULL", 2, "RED", "BIG")
bull.Stay("House")
bull.Brank()
