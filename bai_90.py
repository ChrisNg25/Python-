'''
Viết chương trình in list sau khi đã xóa giá trị 24 trong [12,24,35,24,88,120,155]. Gợi ý:
 
 Sử dụng phương thức xóa của list để xóa giá trị.'''
lis = [12,24,35,24,88,120,155]
print([x for x in lis if x!=24])
