message = "Hello's World "
print(message)
#chuỗi nhiều dòng
message1 = """ Hi, I'm Tuan Anh
and I 21 years old """ 
print(message1)
#độ dài chuỗi
str = 'Tuan Anh dep trai '
print(len(str))
#chỉ mục của chuỗi
str = 'La Tuan Anh'
print(str[0])  # in ra ký tự đầu tiên
print(str[-1])  # in ra ký tự cuối cùng
#cắt lát các chỉ mục
str = 'La Tuan Anh'
print(str[1:5])  # in ra các ký tự từ chỉ mục 1 đến 4
print(str[:5])  # in ra các ký tự từ đầu đến chỉ mục 4
print(str[5:])  # in ra các ký tự từ chỉ mục 5 đến cuối cùng
#chữ hoa chữ thường
str = 'La Tuan Anh'
print(str.lower()) # in ra chuỗi chữ thường
print(str.upper()) # in ra chuỗi chữ hoa
#đếm số kí tự trong chuỗi
str = 'La Tuan Anh'
print(str.count('h')) 
#tìm số chỉ mục của các kí tự nhất định
str = 'La Tuan Anh'
print(str.find('Anh')) # in ra chỉ mục của ký tự đầu tiên của 'Anh' #8
#thay thế kí tự trong chuỗi
str = 'La Tuan Anh'
print(str.replace('Anh', 'Tuan')) # in ra chuỗi mới với 'Anh' được thay thế bằng 'Tuan'
#nhiều chuỗi và nối chuỗi lại với nhau
str1 = 'La Tuan'
str2 = 'Anh'
str = str1 + ' ' + str2 + ', hân hạnh được gặp mặt !'
print(str)
#chèn giá trị vào chuỗi
str1 = 'La Tuan Anh'
str2 = 'dep trai'
str = '{} {}. rat vui duoc gap ban'.format(str1, str2)
print(str)
#f-strings
str1 = 'Cu'
str2 = 'Tuan Anh'
str = f'{str1.upper()}, ten that la {str2.upper()}, rat vui duoc gap ban'
print(str)
#cung cấp về tất cả thuộc tính và phương thức
name = 'cu'
print(dir(name))
#xem thêm thông tin, chức năng của các phương thức
str = 'cu'
print(help(str.upper))