'''
Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.
Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234 Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
'''
a =str(input("Nhap mot so: "))
print(int(a)+int(a*2)+ int(a*3)+int(a*4))
'''
hoac su dung dạng "{}{}{}{}.fomat(a,a,a,a) "
'''