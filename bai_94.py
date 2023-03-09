'''
Viết chương trình đếm và in số ký tự của chuỗi do người dùng nhập vào. Ví dụ:
Nếu chuỗi nhập vào là quantrimang.com thì đầu ra sẽ là:
q,1 
u,1 
a,2 
n,2 
t,1 
r,1 
i,1
m,2 
g,1 
.,1 
c,1 
o,1
Gợi ý:
 Sử dụng dict để lưu trữ các cặp key/value.
 Sử dụng dict.get() để tra cứu key với giá trị mặc định.
'''
dic = {}
n = input("Nhap vao chuoi cac ky tu: ")
for i in n:
    dic[i] = dic.get(i,0) + 1
print("\n".join(["%s,%s"%(k,v) for k,v in dic.items()]))
