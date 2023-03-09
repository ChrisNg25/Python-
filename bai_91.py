'''
Với 2 list cho trước: [1,3,6,78,35,55] và [12,24,35,24,88,120,155], viết chương trình để tạo list có phần tử là giao của 2 list đã cho.
Gợi ý:
Sử dụng set() và "&=" để thiết lập điểm giao
'''
lis1 = set([1,3,6,78,35,55])
lis2 = set([12,24,35,24,88,120,155])
lis1 &= lis2
li= list(lis1)
print(li)