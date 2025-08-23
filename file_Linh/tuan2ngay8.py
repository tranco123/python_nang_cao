class Dog():
    Dogcout = 0  
    def __init__(self, name, size, age, color):  
        self.name = name
        self.size = size
        self.age = age
        self.color = color
    def Go(self):
        print('I am going run')
    def Stay(self, place):
        print('I am staying at {}'.format(place))
    def Lie(self, place):
        print('I am lying at {}'. format(place))
    def Bark(self):
        print("he he")
    def Eat(self, food):
        print('I am eating {}'. format(food))
    def display(self):
        print(f'Tên: {self.name}')
        print(f'Kích cỡ: {self.size}')
        print(f'Tuổi: {self.age}')
        print(f'Màu sắc: {self.color}')
build = Dog()
build.display()
bull = Dog('Bull', 'Large', 2, "Yellow")  
bull.Go()
bull.Stay('Garden')
bull.Lie('home')
bull.Eat('Pho')
bull.Bark()     