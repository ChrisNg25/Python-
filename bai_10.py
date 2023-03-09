'''Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
 
Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Gợi ý:
 Viết lệnh để nhận giá trị X, Y từ giao diện điều khiển do người dùng nhập vào.'''
input_string = input("Nhập 2 số nguyên theo định dạng X,Y: ")
lst = [int(x) for x in input_string.split(',')]
number_ngang= lst[0]
number_doc= lst[1]
lst_result= [[0 for doc in range(number_doc)] for ngang in range(number_ngang)] # cho ra 1 list gồm x list nhỏ, mỗi list nhỏ có y phần tử, toàn bộ là số 0
print(lst_result)
for ngang in range(number_ngang):
    for doc in range(number_doc):
        lst_result[ngang][doc]= ngang * doc 
print(lst_result) 