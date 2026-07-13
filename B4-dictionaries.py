#dictionaries
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
#lấy giá trị của 1 khóa trong từ điển
print(student['name']) #in ra giá trị của khóa 'name'
#hàm get() trả về giá trị của khóa, nếu khóa không tồn tại sẽ trả về None
print(student.get('age', 21))
#thêm 1 khóa và giá trị vào từ điển
student['phone'] = '2107-2005'
#cập nhật giá trị của khóa trong từ điển
student.update({'name': 'Jane', 'age': 26, 'phone': '2005-2107'})
#xóa 1 khóa và giá trị khỏi từ điển
del student['age']
#xem có bao nhiêu khóa trong từ điển
print(len(student))
#lấy tất cả các khóa trong từ điển
print(student.keys())
#lấy tất cả các giá trị trong từ điển
print(student.values())
#lấy tất cả các cặp khóa và giá trị trong từ điển
print(student.items())
#lặp qua các cặp khóa và giá trị trong từ điển
for keys, values in student.items():
    print(keys, values)