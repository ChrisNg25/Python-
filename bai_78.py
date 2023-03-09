'''
Viết chương trình tạo ngẫu nhiên list gồm 5 số chẵn nằm trong đoạn [100;200]. Gợi ý:
 
 Giống bài 77.
'''

import random
print(random.sample([x for x in range(100,201) if not x%2],5))