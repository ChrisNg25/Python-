'''
Viết một chương trình để tạo tuple khác, chứa các giá trị là số chẵn trong tuple (1,2,3,4,5,6,7,8,9,10) cho trước.
Gợi ý:
 
 Sử dụng for để lặp tuple.
 Sử dụng tuple() để tạo tuple từ list.
'''
tup = (1,2,3,4,5,6,7,8,9,10)
print([x for x in tup if not x%2])