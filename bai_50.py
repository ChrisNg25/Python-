'''
Định nghĩa một class có tên là Vietnam, với static method là printNationality. 
Gợi ý:
Sử dụng @staticmethod để định nghĩa class với static method.
'''
class Vietnam (object):
    @staticmethod
    def printNationality ():
        print ("Vietnam")

VietnamVodich = Vietnam ()
VietnamVodich.printNationality ()
Vietnam.printNationality ()