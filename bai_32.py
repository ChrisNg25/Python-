'''
Định nghĩa một hàm có thể in dictionary chứa key là các số từ 1 đến 3 (bao gồm cả hai số) và các giá trị bình phương của chúng.
Gợi ý:
 
 Sử dụng dict[key]=value để nhập mục vào dictionary.
 Sử dụng toán từ ** để lấy bình phương của một số.
'''

def dict_binhphuong():
    d =dict()
    for i in range(1,4):
        d[i]= i**2
    return (d)
print(dict_binhphuong())
        