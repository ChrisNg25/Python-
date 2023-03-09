'''
Viết các lệnh assert để xác minh rằng tất cả các số trong list [2,4,6,8] là chẵn. Gợi ý:
 
 Sử dụng assert để khẳng định.
'''
li = [2,4,6,8,9]
for i in li:
    assert i%2==0, " Trong list co it nhat 1 so le"
try:
    print(li)
except AssertionError as msg:
    print(msg)
