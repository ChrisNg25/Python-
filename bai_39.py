'''
Định nghĩa một hàm có thể tạo list chứa giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20). Sau đó in tất cả các giá trị của list, trừ 5 mục đầu tiên.
Gợi ý:
Tương tư bài 37, 38.
'''
def tinh_binhphuong():
    lis =[ x**2 for x in range(1,21)]
    print(lis[5:])

tinh_binhphuong()