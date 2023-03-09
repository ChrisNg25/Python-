'''
Định nghĩa một hàm có thể tạo và in list chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20).
Gợi ý:
 
 Sử dụng toán tử ** để lấy giá trị bình phương.
 Sử dụng range() cho vòng lặp.
 Sử dụng list.append() để thêm giá trị vào list.
'''
def tinh_binhphuong():
    lst= []
    for x in range(1,21):
        lst.append(x**2)
    print(lst)
tinh_binhphuong()