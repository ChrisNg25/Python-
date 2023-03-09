'''
Viết chương trình để giải 1 câu đố cổ của Trung Quốc: Một trang trại thỏ và gà có 35
 
đầu, 94 chân, hỏi số thỏ và gà là bao nhiêu? Gợi ý:
 Sử dụng vòng lặp for để lặp qua tất cả các giả thuyết có thể.
'''

def tinh_thoga(x,y):
    for i in range(x+1):
        j = x -i
        if (j*4 + i*2) == y:
            return "{} con ga, {} con tho".format(i, j) 
print(tinh_thoga(35,94))

"""def giai(dau,chan):
    klg='Không có dáp án phù hợp!'  
    for i in range(dau+1): 
        j=dau-i
        if 2*i+4*j==chan:
            return i,j
                return klg,klg
# Code by Quantrimang.com
dau=35
chan=94 
dap_an=giai(dau,chan) 
print (dap_an)
"""
