'''Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7.
Gợi ý:
Sử dụng yield.'''




def ham_input(n):
    i = 0
    while i<=n: 
        j = i
        i += 1
        if not j%7:
            yield j

for i in ham_input(100):
    print(i)