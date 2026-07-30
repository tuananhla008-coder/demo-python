'''Python chạy thử code trong khối try
Nếu không có lỗi → bỏ qua toàn bộ except, chạy tiếp code sau đó bình thường
Nếu có lỗi xảy ra → Python lập tức nhảy vào khối except tương ứng, chạy 
code xử lý ở đó, không làm crash chương trình'''
#Ví dụ nếu chưa gắn try/except chương trình dưới đây sẽ báo lỗi vì không
#xuất hiện file 'newnames.csv' trong thư mục
#f = open('newnames.csv')
#print(f)

#Ví dụ gán try/except ở cùng đoạn mã như trên dù lỗi nhưng chương trình vẫn chạy bình thường
try:
    f = open('newnames.csv')
except:
    print('Xin lỗi!Không tồn tại file này')    

try:
    f = open('new_names.csv')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist')
except Exception:
    print('Sorry. Something went wrong.')
'''đoạn mã này sẽ chạy từng dòng try để thử xem đoạn có lỗi không
nếu khi chạy FileNotFoundError mà không xuất hiện file lỗi nào thì sẽ except
tiếp dòng dưới để chấp nhận tất cả các lỗi khác xảy ra và cuối cùng 
phát hiện lỗi giá trị bad_vả không được khai báo  '''

#nếu muốn chương trình chỉ cần in ra lỗi là gì thì hãy đặt tên:
try:
    f = open('new_names.csv')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

#else sẽ chạy nếu chương trình in ra không có lỗi
try:
    f = open('new_names.csv')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.readlines())
    f.close() 

#finally sẽ chạy khi bất cứ điều gì xảy ra dù có thành công hay không  
try:
    f = open('new_names.csv')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.readlines())
    f.close() 
finally:
    print('Dù các dòng trên có lỗi hay không thì khi in ra vẫn chạy finally bình thường')         