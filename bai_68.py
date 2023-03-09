'''
Viết chương trình sử dụng generator để in số chẵn trong khoảng từ 0 đến n, cách nhau bởi dấu phẩy, n là số được nhập vào.
Ví dụ nếu n=10 được nhập vào thì đầu ra của chương trình là: 0,2,4,6,8,10 Gợi ý:
 
 Sử dụng yield để tạo ra giá trị kết tiếp trong generator.
'''

n = int(input("Nhap so nguyen: "))
def even_generator(n):
    i = 0
    while i<=n:
        if not i%2:
            yield i
        i +=1
values = [str(x) for x in even_generator(n)]
print(",".join(values))
