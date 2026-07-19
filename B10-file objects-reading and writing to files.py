#phương pháp mở tập tin bằng trình quản lý ngữ cảnh từ bên trong python
with open('text.txt', 'r') as f:
   # f_contents = f.read()
  #  print(f_contents)
 #đọc các dòng
    #f_contents = f.readlines()
    #print(f_contents)
    #đọc từng dòng
    #f_contents = f.readline()
    #print(f_contents)
    #đọc các tệp có dữ liệu lớn
    #for line in f:
       # print(line, end='')

    #chỉ định dữ liệu mỗi lần đọc
    #f_contents = f.read(21)
    #print(f_contents, end='')
    #sử dụng vòng lặp để lặp qua từng phần nhỏ 1
    '''size_to_read = 7
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='+')
        f_contents = f.read(size_to_read)'''

#phương pháp ghi 
'''with open('test3.txt', 'w') as f:
    f.write('tét')
    f.seek(2) #ghi đè 
    f.write('s')'''
#phương pháp ghi và đọc kết hợp
with open ('text.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
#làm việc với hình ảnh
with open ('tuananh.jpg', 'rb') as rf:
    with open ('tuananh_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

