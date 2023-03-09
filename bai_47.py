'''
Viết chương trình Python dùng map() và filter() để tạo list chứa giá trị bình phương của các số chẵn trong [1,2,3,4,5,6,7,8,9,10].
Gợi ý:
 
 Dùng map() để tạo list.
 Dùng filter() để lọc thành phần trong list.
 Dùng lambda để định nghĩa hàm chưa biết.
'''
lis= [1,2,3,4,5,6,7,8,9,10]
#sochan= list(filter(lambda x: not x%2,lis))
#binhphuong = list(map(lambda x: x**2, sochan))
binhphuong = list(map(lambda x: x**2, list(filter(lambda x: not x%2,lis))))
print(binhphuong)