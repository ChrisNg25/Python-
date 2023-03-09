'''
Viết một chương trình Python nhận chuỗi nhập vào bởi người dùng, in "Yes" nếu chuỗi là "yes" hoặc "YES" hoặc "Yes", nếu không in "No".
Gợi ý:
  
 Sử dụng lệnh if để kiểm tra điều kiện.
'''

s = input("Nhap lenh YES/NO: ")
if s == "yes" or s == "YES" or s == "Yes":
    print("Yes")
else: 
    print("No")