'''
Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.
Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9
Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
'''
items = [x for x in input("Nhap chuoi cac day so: ").split(",")]
lst = []
for i in items:
    if not int(i)%2:
        pass
    else:
        lst.append(i)
#lst = [x for x in input("Nhập dãy số của bạn, cách nhau bởi dấu phẩy: ").split(",") if int(x)%2!=0]
print(",".join(lst))