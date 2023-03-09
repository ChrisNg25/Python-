'''
Định nghĩa một hàm có input là 2 chuỗi và in chuỗi có độ dài lớn hơn trong giao diện điều khiển. Nếu 2 chuỗi có chiều dài như nhau thì in tất cả các chuỗi theo dòng.
Gợi ý:
 
Sử dụng hàm len() để lấy chiều dài của một chuỗi
'''
def sosanh_dodai(a,b):
    if len(str(a)) == len(str(b)):
        print(str(a))
        print(str(b))
    elif len(str(a)) > len(str(b)):
        print(str(a))
    else: 
        print(str(b))
    
sosanh_dodai("aaaaaa","ffgfgdfe")