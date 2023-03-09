'''
Viết chương trình Python có thể lọc các số chẵn trong danh sách sử dụng hàm filter. Danh sách là [1,2,3,4,5,6,7,8,9,10].
Gợi ý:
 
 Sử dụng filter() để lọc các yếu tố trong một list.
 Sử dụng lambda để định nghĩa hàm chưa biết.
'''

lis = [1,2,3,4,5,6,7,8,9,10]
sochan = list(filter(lambda x: x%2 == 0, lis))
print(sochan)
