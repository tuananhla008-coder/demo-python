def hello_func():
   # pass #không muốn làm gì với hàm nhưng nó sẽ không báo lỗi
    print('Hello function')
hello_func()    
#giá trị trả về
def hello_func():
    return 'Hello function'
print(hello_func())
#trả về giá trị tham số
#đối với format
def hello_func(greeting, name='you'):
    return'{}, {}'.format(greeting, name)
print(hello_func('Hi'))
#đối với f-strings
def hello_func(greeting, name='cu'):
    f'{greeting}, {name}'
print(hello_func('Hi'))    

