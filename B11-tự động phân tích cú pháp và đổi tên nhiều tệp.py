#đổi tên và sắp xếp lại thứ tự tệp
import os
os.chdir(r'C:\Users\Cu\OneDrive\Documents\demo python\images')

#print(os.getcwd())
for f in os.listdir():#nêu tất cả tệp ra 
    #print(os.path.splitext(f)) #tách phần mở rộng ra khỏi tên tệp
    f_name, f_ext = os.path.splitext(f)
    #print(file_name) #in phần tên tệp 
    f_title, f_course, f_num = f_name.split('-') #tách các mục nhỏ trong phầ tên tệp
    #print(f_num)
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2) #tạo chuỗi có kí tự 0 đệm 
   # print('{}-{}-{}{}' .format(f_course, f_num, f_title, f_ext)) #thay đổi vị trí các mục nhỏ của tên tệp theo ý muốn cuẩ mình
    new_images = '{}-{}{}'.format(f_num, f_title, f_ext) 
    os.rename(f, new_images)
