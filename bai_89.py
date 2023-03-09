'''
Viết chương trình in list sau khi đã xóa số ở vị trí thứ 0, thứ 4, thứ 5 trong [12,24,35,70,88,120,155].
Gợi ý:
 
 Giống bài 87.
'''
lis= [12,24,35,70,88,120,155]
print([x for i,x in enumerate(lis) if i != 0 and i!=4 and i!=5 ]) # if i not in (0,4,5)
