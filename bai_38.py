'''
Định nghĩa một hàm có thể tạo ra list chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20), rồi in 5 mục cuối cùng trong list.
Gợi ý:
Tương tự bài 37.
'''
def tinh_binhphuong():
    lis=[ x**2 for x in range(1,21)]
    print(lis[-5:])
tinh_binhphuong()