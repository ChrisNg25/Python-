'''Định nghĩa một class có ít nhất 2 method:
getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển. printString: in chuỗi vừa nhập sang chữ hoa.
Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.
Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM Gợi ý:
 
 Sử dụng __init__ để xây dựng các tham số.'''

class Input_OutString():
    def __init__(self):
        self.str = ""

    def get_string(self):
        self.str = input("Nhập 1 string: ")

    def upper_string(self):
        return self.str.upper()

strObj = Input_OutString()
strObj.get_string()
print("Chuoi chu in hoa: ",strObj.upper_string())

