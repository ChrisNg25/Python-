'''
Viết chương trình tính: f(n)=f(n-1)+100 khi n>0 và f(0)=1, với n là số được nhập vào (n>0).
 
Ví dụ: Nếu n được nhập vào là 5 thì đầu ra phải là 500. Gợi ý:
 Chúng ta có thể định nghĩa hàm đệ quy trong Python.
'''

s= int(input("Nhap so nguyen: "))

def ham_f(s):
    if s == 0:
        return 1
    elif s >0 : 
        return ham_f(s-1) + 100
print(ham_f(s))