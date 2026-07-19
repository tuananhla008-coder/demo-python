import os
'''print(os.getcwd()) #in ra thư mục hiện tại mà chúng ta đang ở'''
os.chdir('C:/Users/Cu/OneDrive/Desktop') #điều hướng thư mục
'''print(os.getcwd())'''
#os.makedirs('cu.jpg-2/Sub-Dir-1') #tạo thư mục mới
#os.removedirs('cu.jpg-2/Sub-Dir-1') #xóa 1 thư mục duy nhất
#os.rename('cu.jpg', 'tuananh.jpg')#đổi tên tệp, thư mục
#print(os.listdir()) #liệt kê thư mục và tập tin
print(os.stat('tuananh.jpg').st_size)# in ra thông tin về tệp, thư mục

# Tạo thư mục test ngoài OneDrive để xóa thư mục
'''import os, shutil
os.makedirs('C:/pytest_playground', exist_ok=True)
os.chdir('C:/pytest_playground')
print("Đang ở:", os.getcwd())

os.makedirs('cu.jpg-2/Sub-Dir-1')
print(os.listdir())

shutil.rmtree('cu.jpg-2')
print("Xóa xong")'''

#muốn xem ở định dạng ngày giờ thực tế
'''import os
from datetime import datetime
mod_time = os.stat('tuananh.jpg').st_mtime
print(datetime.fromtimestamp(mod_time))'''

#duyệt qua cây thư mục và in tất cả các thư mục và tệp
import os
for dirpath, dirnames, filenames in os.walk('C:/Users/Cu/OneDrive/Desktop'):
    print('Thư mục lớn là:', dirpath)
    print('Thư mục con là:', dirnames)
    print('Tệp là:', filenames)
    print()

#truy cập vị trí thư mục chính bằng cách lấy biến môi trường
import os
os.chdir('C:/Users/Cu/OneDrive/Desktop')
print(os.environ.get('USERPROFILE'))
#sử dụng USERPROFILE để tạo 1 tệp mới trong thư mục chính
import os
os.chdir('C:/Users/Cu/OneDrive/Desktop')
file_path = os.path.join(os.environ.get('USERPROFILE'), 'TEST.txt') #os.path.join là phép nối hệ điều hành
print(file_path)

#1 số phương pháp trong đường dẫn hệ điều hành
# kiểm tra đường dẫn có tồn tại hay không
print(os.path.exists('/tmp/test.txt'))
