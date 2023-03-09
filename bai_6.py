'''
Viết một method tính giá trị bình phương của một số. Gợi ý:
 
 Sử dụng toán tử **.'''

x=int(input("Nhap so nguyen: "))
def binhphuong(a):
    return a**2
print("So nguyen: ", x)
print("Binh phuong cua so nguyen: ",binhphuong(x))