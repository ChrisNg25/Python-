'''
Định nghĩa một class có tên là Circle có thể được xây dựng từ bán kính. Circle có một method có thể tính diện tích.
Gợi ý:
Sử dụng def methodName(self) để định nghĩa method.
'''

class Circle:

    def __init__(self, r):
        self.ban_kinh = r

    def square_circle(self):
        return self.ban_kinh **2 *3.14

hinhtron = Circle(2)
print(hinhtron.square_circle())