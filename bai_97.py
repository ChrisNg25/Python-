'''
Viết chương trình in tất cả các hoán vị của [1,2,3]. Gợi ý:
 
 Sử dụng itertools.permutations() để lấy hết các hoán vị của list.
'''
import itertools 

print(list(itertools.permutations([1,2,3])))