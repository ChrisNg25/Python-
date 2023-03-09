'''
Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển.
Định dạng nhật ký được hiển thị như sau:
D 100 W 200
(D là tiền gửi, W là tiền rút ra). Giả sử đầu vào được cung cấp là: D 300
 
D 300
W 200
D 100
Thì đầu ra sẽ là: 500
Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
'''
money_inbank = 0
while True:
    s = input("Nhap thong tin giao dich: ")
    if not s:
        break
    thongtin_giaodich = s.split(" ")
    sotien_giaodich = thongtin_giaodich [1]
    giaodich = thongtin_giaodich [0]
    if giaodich == "D":
        money_inbank += int(sotien_giaodich)
    elif giaodich == "W":
        money_inbank -= int(sotien_giaodich)
    else:
        pass
print("So tien trong tai khoan: ",money_inbank)