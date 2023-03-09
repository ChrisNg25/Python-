'''
Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường. Giả sử đầu vào là: Quản Trị Mạng
Thì đầu ra là:
Chữ hoa: 3
Chữ thường: 8 Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
'''

s = input("Nhap mot chuoi cac ky tu: ")
d = {"Upper": 0, "Lower": 0}
for i in s:
    if i.isupper():
        d["Upper"] +=1
    elif i.islower():
        d["Lower"] +=1
    else:
        pass
print("Số chữ thường: ", d["Lower"])
print("Số chữ hoa: ", d["Upper"])
