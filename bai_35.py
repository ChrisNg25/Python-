'''
Định nghĩa một hàm có thể tạo ra một dictionary chứa key là những số từ 1 đến 20 (bao gồm cả 1 và 20) và các giá trị bình phương của key. Hàm chỉ cần in các key.
Gợi ý:
Tương tự như bài 34.
'''
def print_key():
    d= dict()
    for i in range(1,21):
        d[i] = i**2
    for k,v in d.keys(): #for k,v in d.items():
        print(k)
print_key()