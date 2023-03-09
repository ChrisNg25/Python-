'''
Viết một chương trình để tạo ra và in tuple chứa các số chẵn được lấy từ tuple (1,2,3,4,5,6,7,8,9,10).
Gợi ý:
 
 Sử dụng "for" để lặp lại tuple.
 Sử dụng tuple() để tạo ra một tuple từ một danh sách.
'''

tup = (1,2,3,4,5,6,7,8,9,10)
print(tuple([x for x in tup if not x%2]))