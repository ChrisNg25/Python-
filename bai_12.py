'''
Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa và in ra màn hình. Giả sử đầu vào là:
Hello world
Practice makes perfect
Thì đầu ra sẽ là:
HELLO WORLD
PRACTICE MAKES PERFECT
Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
'''
lines= []
while True:
    input_string = input("Nhap mọt chuoi cac ky tu: ")
    if input_string:
        lines.append(input_string.upper())
    else: 
        break
for sentence in lines:
    print(sentence)

