'''
Định nghĩa một hàm có thể in dictionary chứa các key là số từ 1 đến 20 (bao gồm cả 1 và 20) và các giá trị bình phương của chúng.
Gợi ý:
   
 Sử dụng dict[key]=value để nhập mục vào dictionary.
 Sử dụng toán từ ** để lấy bình phương của một số.
 Sử dujnng range() cho các vòng lặp.
'''
def dict_binhphuong():
    d= dict()
    for i in range(1,21):
        d[i] = i**2
    print(d)
dict_binhphuong()