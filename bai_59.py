'''
Tương tự như bài 58, nhưng lần này ta sẽ viết hàm để lấy companyname. Gợi ý:
 
 Giống bài 58.'''

import re
emailAddress = input("Nhap dia chi email: ")
pat2= "(\w+)@(\w+)\.(com)"
r2= re.match(pat2,emailAddress)
print(r2.group(2))