'''
Định nghĩa một class có tên là Shape và class con là Square. Square có hàm init để lấy đối số là chiều dài. Cả 2 class đều có hàm area để in diện tích của hình, diện tích mặc định của Shape là 0.
Gợi ý:
 
Để ghi đè một method trong super class, chúng ta có thể định nghĩa một method có cùng tên trong super class.
'''
class Sharp:
    def __init__(self):
        pass

    def area(self):
        return 0
class Square(Sharp):
    def __init__(self, l):
        Sharp.__init__(self)
        self.lenght = l
    def area(self):
        return self.lenght**2
    
aSquare = Square(3)
print(aSquare.area())
