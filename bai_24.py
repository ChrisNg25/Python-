'''
Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm đầu tiên (0,0). Robot có thể di chuyển theo hướng UP, DOWN, LEFT và RIGHT với những bước nhất định. Dấu di chuyển của robot được đánh hiển thị như sau:
 
UP 5 DOWN 3 LEFT 3 RIGHT 3
Các con số sau phía sau hướng di chuyển chính là số bước đi. Hãy viết chương trình để tính toán khoảng cách từ vị trí hiện tại đến vị trí đầu tiên, sau khi robot đã di chuyển một quãng đường. Nếu khoảng cách là một số thập phân chỉ cần in só nguyên gần nhất.
Ví dụ: Nếu tuple sau đây là input của chương trình:
UP 5 DOWN 3 LEFT 3 RIGHT 2
thì đầu ra sẽ là 2.'''
import math
buoc_len = 0
buoc_ngang = 0
while True: 
    s = input("Nhap thong tin di chuyen cua robot: ")
    if not s:
        break
    dichuyen = s.split(" ")
    huong_dichuyen = dichuyen[0]
    buoc_dichuyen =  dichuyen[1]
    
    if huong_dichuyen == "UP":
        buoc_len += int(buoc_dichuyen)
    elif huong_dichuyen == "DOWN":
        buoc_len -= int(buoc_dichuyen)
    elif huong_dichuyen == "LEFT":
        buoc_ngang -= int(buoc_dichuyen)
    elif huong_dichuyen == "RIGHT":
        buoc_ngang += int(buoc_dichuyen)
    else: 
        pass
print("Khoang cach di chuyen cua Robot la: ", round(math.sqrt(buoc_len**2 + buoc_ngang**2)))
