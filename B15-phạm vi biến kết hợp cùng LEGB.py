#LEGB = local(cục bộ), enclosing(bao quanh), global(toàn cục), built-in(tích hợp sẵn)
'''
local - biến khai báo bên trong hàm đang chạy
enclosing - biến ở hàm cha bao ngoài(khi có hàm lồng nhau)
global - biến khai báo ở ngoài cùng file, không nằm trong hàm nào
built-in - các tên có sẵn của python(print, len, str,...)
'''
x = 'global x' 
'''nếu vô hiệu hóa biến ngoài này nhưng trong hàm vẫn còn biến toàn cục 
thì hàm vẫn chạy bình thường nếu vô hiệu hóa cả 2 thì hàm sẽ không chạy'''

def test():
     #global x #nếu gọi biến toàn cục trong hàm thì khi in ra sẽ in ra giá trị là local x
     x = 'local x' 
     print(x)
     '''y = 'local y'
     print(y)
     print(x) #vẫn sẽ in ra global x'''
test()   
#print(y) #sẽ báo lỗi vì biến y chỉ xuất hiện bên trong local không chạy được bên ngoài
print(x)
#hàm tích hợp sẵn
m = max([7, 21, 20, 5])
print(m)
#muốn xem phạm vi thuộc tính của built-in
import builtins
print(dir(builtins))
#tránh ghi đè khi sử dụng hàm tích hợp sẵn
def min(): #nếu để thành my_min thì hàm chạy bình thường
    '''hàm sẽ báo lỗi bởi vì chương trình 
    đã tìm thấy min ở biến toàn cục sẽ không tìm đến hàm tích hợp nữa'''
    pass #câu lệnh rỗng dùng để giữ chỗ để chương trình không bị lỗi cú pháp
m = max([7, 21, 20, 5])
print(m)
#E hàm lồng nhau, hàm bao quanh
def outer():
     x = 'outer x' #nếu vô hiệu hóa dòng này và khôi phục chạy dòng bên tròn sẽ báo lỗi

     def inner():
        #nonlocal x 
        '''khai báo biên toàn cục trong hàm nhưng không được viết global 
        mà viết nonlocal'''
        x = 'inner x' 
        '''#nếu vô hiệu hóa dòng này thì biến vẫn sẽ in ra outer x 2 lần 
        đó chính là sự đặc biệt của phạm vi bao trùm
        '''
        print(x)
     inner()
     print(x)
outer() 
'''LƯU Ý: nếu khi các giá trị bên trong hàm bị vô hiệu hóa thì khi in ra giá trị
      sẽ in ra giá trị của biến toàn cục  '''