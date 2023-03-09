'''
Viết chương trình in list sau khi đã xóa số thứ 0, thứ 2, thứ 4, thứ 6
 
trong [12,24,35,70,88,120,155]. Gợi ý:
 Sử dụng list comprehension để xóa một loạt phần tử trong list.
 Sử dụng hàm enumerate() để lấy index, value của tuple.
'''
lis = [12,24,35,70,88,120,155]
count= [i for x,i in enumerate(lis) if x%2]
print(count)