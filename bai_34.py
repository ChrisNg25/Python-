'''
Định nghĩa một hàm có thể tạo dictionary, chứa các key là số từ 1 đến 20 (bao gồm cả 1 và 20) và các giá trị bình phương của chúng. Hàm chỉ in các giá trị mà thôi.
Gợi ý:
 
 Sử dụng dict[key]=value để nhập mục vào dictionary.
 Sử dụng toán từ ** để lấy bình phương của một số.
 Sử dụng range() cho các vòng lặp.
 Sử dụng keys() để di lặp các key trong dictionary. Có thể sử dụng item() để nhận
cặp key/value.
'''
def print_value():
    d=dict()
    for i in range(1,21):
        d[i] = i**2
    for k,v in d.items():
        print(v)
print_value()