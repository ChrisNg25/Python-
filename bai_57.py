'''
Định nghĩa một class exception tùy chỉnh, nhận một thông báo là thuộc tính. Gợi ý:
  
 Để định nghĩa một class exception tùy chỉnh, chúng ta phải định nghĩa một class kế thừa từ Exception.
'''
class MyError(Exception):
     """My own exception class
     Attributes:
        msg -- explanation of the error
     """
     def __init__(self, msg):
        self.msg = msg
error = MyError("Có gì đó sai sai!")
print (error)