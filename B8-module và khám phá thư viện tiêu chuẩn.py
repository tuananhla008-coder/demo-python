import my_module as mm #'as mm' là kí hiệu thay thế cho my_module
courses = ['History', 'Math', 'Physical', 'Music']
index = mm.find_index(courses, 'Music')
print(index)
#import 1 hàm 
from my_module import find_index
courses = ['History', 'Math', 'Physical', 'Music']
index = find_index(courses, 'Music')
print(index)
#import nhiều hàm
from my_module import find_index, test
courses = ['History', 'Math', 'Physical', 'Music']
index = find_index(courses, 'Music')
print(index)
print(test)
#import tất cả sẽ bị hạn chế dùng vì không hiệu quả
from my_module import *
courses = ['History', 'Math', 'Physical', 'Music']
index = find_index(courses, 'Music')
print(index)
print(test)
#cách tìm vị trí các module
from my_module import find_index, test
import sys
courses = ['History', 'Math', 'Physical', 'Music']
index = find_index(courses, 'Music')
print(index)
print(test)
#cách sử dụng thư viện chuẩn
import sys
sys.path.append(r'C:\Users\Cu\OneDrive\Documents\my_modules')
from my_module import find_index, test

courses = ['History', 'Math', 'Physical', 'Music']
index = find_index(courses, 'Music')
#print(index)
#print(test)
print(sys.path)
''' trong trường hợp muốn tìm lại file khi đã thay đổi thư viện thì cần xóa hết những đoạn mã code khác và chỉ để lại
đoạn mã code import sys thôi '''
#module ngẫu nhiên
import random
courses = ['History', 'Math', 'Physical', 'Music']
random_courses = random.choice(courses)
print(random_courses)
#1 số module hữu ích
import math #module toán học
rads = math.radians(120)
print(rads)

import datetime #làm việc với ngày và giờ
today = datetime.date.today()
print(today)

import os 
print(os.getcwd())#in ra thư mục làm việc hiện tại
print(os.__file__)#xác định vị trí của 1 module