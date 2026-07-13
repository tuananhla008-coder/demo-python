#câu lệnh if/else/elif
language = 'java'
if language == 'python':
    print('Language is python')
elif language == 'java':
    print('language is java')    
else:
    print('No language')    
#1 số phép toán boolean
#and nếu cả 2 giá trị đều đúng thì mới True
#or nếu 1 trong 2 giá trị đúng thì True
#not sẽ đảo ngược True thành False và ngược lại
user = 'admin'
loggin = True
if user == 'admin' and loggin:
    print('thành công')
else:
    print('thất bại')   
#kiểm tra xem 2 đối tượng có giống nhau k
a = [1, 2, 3]
b = [1, 2, 3] 
print(a == b)
print(a is b) #sẽ trả về True bời vì a và b là 2 đối tượng khác nhau 
#nếu muốn a is b = True 
a = [1,2,3]
a = b
print(id(a))
print(id(b))
print(a is b)
# Các khả năng xảy ra giá trị là False:
#False
#None
#Số 0 của bất kì kiểu số nào
#Bất kì chuỗi rỗng nào, ví dụ: '' [] ()
#Bất kì ngoặc rỗng nào, ví dụ: {}
