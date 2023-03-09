'''

Viết chương trình để tạo ngẫu nhiên một list gồm 5 số, chia hết cho 5 và 7, nằm trong đoạn [1;1000].
Gợi ý:
 
 Giống bài 77, 78.
'''
import random 
print(random.sample([x for x in range(1,1001) if not x%5 and not x%7],5))