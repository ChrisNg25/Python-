'''
Định nghĩa class Nguoi và 2 class con của nó: Nam, Nu. Tất cả các class có method "getGender" có thể in "Nam" cho class Nam và "Nữ" cho class Nu.
Gợi ý:
 
 Sử dụng Subclass(Parentclass) để định nghĩa 1 class con.'''

class Nguoi:
    def getGender(self):
        return " None"
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nu"
na=Nam()
nu=Nu()
print(na.getGender())
print(nu.getGender())