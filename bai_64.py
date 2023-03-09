'''
Viết chương trình tính: f(n)=f(n-1)+100 khi n>0 và f(0)=1, với n là số được nhập vào (n>0).
 
Ví dụ: Nếu n được nhập vào là 5 thì đầu ra phải là 500. Gợi ý:
 Chúng ta có thể định nghĩa hàm đệ quy trong Python.
'''
def f(n):
    if n == 0:
        return 1
    elif int(n) > 0:
        return int(f(n-1)) + 100
    
print(f(int(input("Nhap vao so nguyen: "))))