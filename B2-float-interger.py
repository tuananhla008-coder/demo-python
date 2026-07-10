#xác định kiểu dữ liệu
num1 = 21 #số nguyên
num2 = 7.25 #số thực
print(type(num1))
print(type(num2))
#các phép toán tử số học
print(3+2)#cộng #5
print(3-2)#trừ #1
print(3*2)#nhân #6
print(3/2)#chia #1.5
print(3//2)#chia lấy phần nguyên #1
print(3**2)#lũy thừa #9
print(3%2)#chia lấy phần dư #1
#làm tăng giá trị của hàm
num = 5
num += 3 #tăng giá trị của num lên 3 #8
num -= 2 #giảm giá trị của num đi 2 #3
num *= 4 #nhân giá trị của num với 4 #20
num /= 2 #chia giá trị của num cho 2 #2.5
#hàm giá trị tuyệt đối
print(abs(-5)) #5
#hàm làm tròn đến giá trị nguyên gần nhất
print(round(3.7)) #4
#toán tử so sánh
print(3 > 2) #True #so sánh lớn hơn
print(3 < 2) #False #so sánh nhỏ hơn
print(3 == 2) #False #so sánh bằng nhau
print(3 != 2) #True #so sánh không bằng nhau
print(3>= 2) #True #so sánh lớn hơn hoặc bằng
print(3<= 2) #False #so sánh nhỏ hơn hoặc bằng
#ép kiểu
num1 = '21'
num2 = '7.25'
print(int(num1)) #21
print(float(num2)) #7.25
num1 = int(num1)
num2 = float(num2)
print(num1 + num2)