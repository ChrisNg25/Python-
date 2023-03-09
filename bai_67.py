'''
Dãy Fibonacci được tính dựa trên công thức sau:
f(n)=0 nếu n=0
f(n)=1 nếu n=1
f(n)=f(n-1)+f(n-2) nếu n>1
Hãy viết chương trình sử dụng list comprehension để in dãy Fibonacci dưới dạng tách biệt bằng dấu ",", n được người dùng nhập vào.
Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của chương trình sẽ là: 0,1,1,2,3,5,8,13 Gợi ý:
 Chúng ta có thể định nghĩa hàm đệ quy trong Python.
 Sử dụng list comprehension để tạo ra list từ list hiện có.
 Sử dụng string.join() để nối danh sách các chuỗi.
'''
n= int(input("Nhap so nguyen: "))
def ham_f(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n >1: return ham_f(n-1) + ham_f(n-2)

values = [str(ham_f(x)) for x in range(n+1) ]
print(",".join(values))
