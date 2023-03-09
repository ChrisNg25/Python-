'''
Viết chương trình in list sau khi xóa các số chẵn trong [5,6,77,45,22,12,24]. Gợi ý:
 
 Sử dụng list comprehension để xóa một loạt phần tử của list.
'''
lis= [5,6,77,45,22,12,24]
print([x for x in lis if x%2])