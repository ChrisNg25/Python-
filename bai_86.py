'''
Sử dụng list comprehension để viết chương trình in list sau khi đã loại bỏ các số chia hết cho 5 và 7 trong [12,24,35,70,88,120,155].
Gợi ý:
 Giống bài 85.'''

lis =[12,24,35,70,88,120,155]
print([x for x in lis if x%5 and x%7])