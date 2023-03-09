'''
Định nghĩa class có tên là Hinhchunhat được xây dựng bằng chiều dài và chiều rộng. Class Hinhchunhat có method để tính diện tích.
Gợi ý:
 
 Như bài 52.
'''
class Hinhchunhat():

    def __init__(self, d, r):
        self.dai = d
        self.rong =r 

    def dientich_hinhchunhat(self):
        return "Dien tich hinh chu nhat co canh {} và {} là {}".format(self.dai,self.rong,self.dai * self.rong)
    
aHinhchunhat = Hinhchunhat(2,10)
print(aHinhchunhat.dientich_hinhchunhat())