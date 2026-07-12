#lists
courses = ['Math','History','Physical','CompSci']
print(courses)
print(len(courses)) #độ dài của danh sách
#truy cập từng giá trị trong danh sách
print(courses[0]) #in ra giá trị đầu tiên
print(courses[1]) #in ra giá trị thứ hai
print(courses[2]) #in ra giá trị thứ ba
print(courses[3]) #in ra giá trị thứ tư
print(courses[-1]) #in ra giá trị cuối cùng
print(courses[0:3]) #in ra các giá trị từ chỉ mục 0 đến 2
print(courses[:3]) #in ra các giá trị từ chỉ mục 0 đến 2
print(courses[1:]) #in ra các giá trị từ chỉ mục 1 đến cuối cùng
#thêm giá trị vào danh sách
courses.append('English') #thêm giá trị vào cuối danh sách
print(courses)
courses.insert(0,'Art') #thêm giá trị vào 1 vị trí cụ thể
print(courses)
courses_2 = ['Art', 'Music']
courses.extend(courses_2) #thêm các giá trị từ courses_2 vào courses, thêm nhiều giá trị vào danh sách
print(courses)
#xóa giá trị khỏi danh sách
courses.remove('Math') #xóa giá trị cụ thể khỏi danh sách
courses.pop() #xóa giá trị cuối cùng khỏi danh sách
#sắp xếp danh sách
courses.reverse() #đảo ngược danh sách
courses.sort() #sắp xếp danh sách theo thứ tự tăng dần
courses.sort(reverse = True) #sắp xếp danh sách theo thứ tự giảm dần
nums = [1, 5, 2, 4, 3]
print(min(nums)) #in ra giá trị nhỏ nhất trong danh sách
print(max(nums)) #in ra giá trị lớn nhất trong danh sách
print(sum(nums)) #in ra tổng các giá trị trong danh sách
#tìm chỉ mục của giá trị nhất định
print(courses.index('CompSci')) #in ra chỉ mục của giá trị 'CompSci'
#kiểm tra xem giá trị có trong danh sách hay không
print('History' in courses) #True
#vòng lặp qua danh sách
for item in courses:
    print(item) #in ra từng giá trị trong danh sách

#hàm trả về chỉ mục hiện tại và giá trị
for index, course in enumerate(courses, start = 1):
    print(index, course) #in ra chỉ mục và giá trị hiện tại

#chuyển danh sách thành chuỗi
courses_str = ', '.join(courses)
print(courses_str) #in ra chuỗi các giá trị trong danh sách, cách nhau bởi dấu phẩy
#chuyển chuỗi thành danh sách
new_list = courses_str.split(', ')
print(new_list) #in ra danh sách các giá trị trong chuỗi, cách nhau bởi dấu phẩy

#TUPLES tương đồng với danh sách nhưng không thể sửa đổi bộ dữ liệu
tuple_1 = ('Math','History','Physical','CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
#thay đổi chỉ mục trong tuples
#tuple_1[0] = 'Art' #sẽ báo lỗi vì tuples không thể sửa đổi bộ dữ liệu

#SETS là các giá trị không có thứ tự và không có phần tử trùng lặp
car_set = {'Honda', 'Toyota', 'Ford', 'BMW'}
print(car_set) #in ra các giá trị trong set và không theo thứ tự, liên tục thay đối vị trí
#loại bỏ các giá trị trùng lặp trong set
car_set = {'Honda', 'Toyota', 'Ford', 'BMW', 'Honda', 'Toyota'}
print(car_set) #in ra các giá trị trong set và không có phần tử trùng
#xác định giá trị có trong set hay không
print('Honda' in car_set) #True
#những khóa học nào mà cả 2 tập hợp có chung
course_set_1 = {'Math', 'History', 'Physical', 'CompSci'}
course_set_2 = {'Math', 'History', 'Art', 'Design'}
print(course_set_1.intersection(course_set_2)) #in ra các giá trị chung #{'History', 'Math'}
#những khóa học nào mà 1 tập hợp có nhưng tập hợp còn lại không có
print(course_set_1.difference(course_set_2)) #in ra các giá trị có trong course_set_1 nhưng không có trong course_set_2 #{'Physical', 'CompSci'}
#in ra tất cả các khóa học trong cả 2 tập hợp
print(course_set_1.union(course_set_2)) #in ra tất cả các khóa học trong cả 2 tập hợp