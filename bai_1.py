'''
Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
Gợi ý:
 
 Sử dụng range(#begin, #end)
'''
j=[]
for i in range(2000,3201):
    if i % 7 == 0:
        j.append(str(i))
# nối chuỗi trong Python bằng phuơng thức join()
i=','.join(j) # cách nhau giữa các chuỗi là dấu ","
print(i)
