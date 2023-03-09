'''
Viết chương trình tạo mảng 3D 3*5*8 có mỗi phần tử là 0. Gợi ý:
 
 Sử dụng list comprehension để tạo mảng.
'''
print([[[0 for x in range(8)] for i in range(5)] for j in range(3)])