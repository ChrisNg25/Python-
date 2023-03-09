'''
Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
Thì đầu ra sẽ là:
Số chữ cái là: 10 Số chữ số là: 3
Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
'''
s = input("Nhap chuoi cac ky tu: ")
d = {"Digits": 0, "Letters":0}
for c in s:
    if c.isdigit():
        d["Digits"] +=1
    elif c.isalpha():
        d["Letters"] +=1 
    else:
        pass

print ("Số chữ cái là:", d["Letters"])
print ("Số chữ số là:", d["Digits"])