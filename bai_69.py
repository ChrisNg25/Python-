'''
Viết chương trình sử dụng generator để in số chia hết cho 5 và 7 giữa 0 và n, cách nhau bằng dấu phẩy, n được người dùng nhập vào.
Ví dụ: Nếu n=100 được nhập vào thì đầu ra của chương trình là: 0,35,70. Gợi ý:
Như bài 68.
'''

n = int(input("Nhap so nguyen: "))

def boiso5_7(n):
    i=0
    while i <=n:
        if not i%5 and not i%7:
            yield i  
        i += 1 
values = [str(x) for x in boiso5_7(n)]
print(",".join(values))
