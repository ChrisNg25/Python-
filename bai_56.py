'''
Viết hàm để tính 5/0 và sử dụng try/exception để bắt lỗi. Gợi ý:
 
 Sử dụng try/exception để bắt lỗi.
'''
def chia_0():
    return 5/0

try: 
    chia_0()
except ZeroDivisionError:
    print("Lỗi chia một số cho 0")
except Exception as problem:
    print("Bắt được một Exception")
finally:
    print("Phép tính bị huỷ")

