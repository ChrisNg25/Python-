'''
Vui lòng viết chương trình để xuất một số ngẫu nhiên, chia hết cho 5 và 7, từ 0 đến 200 (gồm cả 0 và 200), sử dụng module random và list comprehension.
Gợi ý:
 
 Giống bài 75.
'''
import random 
print(random.choice([x for x in range(201) if not x%5 and not x%7]))
