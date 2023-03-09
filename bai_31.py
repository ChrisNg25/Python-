'''
Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là một số chẵn" nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ.
Gợi ý:
Sử dụng toán tử % để kiểm tra xem số đó chẵn hay lẻ.
'''
def phanbiet_chanle(a):
    print("Day la so chan" if a%2==0 else "Day la so le")
phanbiet_chanle(11)
