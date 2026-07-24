'''CSV(comma separated values) giá trị được phân tách bằng dấu phẩy cho phép đưa dữ liệu
vào 1 tập tin văn bản thuần túy và sử dụng 1 loại dấu phân cách, thường là dấu phẩy, để phân tách các
trường khác nhau'''
import csv
with open('names.csv', 'r') as csv_file: #cách đọc trong 1 danh sách CSV
    #csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file) 
    '''trình đọc từ điển khi in ra sẽ không xuất hiện tên trường
ở dòng đầu tiên nữa thay vào đó sẽ xuất hiện ở đầu dòng, đầu các ý ở mỗi dòng'''

   #for line in csv_reader:
       #print(line['email'])



    with open('new_names.csv', 'w') as new_file: #tạo file mới để ghi nội dung mới
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        #fieldnames ở bên trái là tham số của Dictwriter còn bên phải là giá trị của biến fieldnames
        csv_writer.writeheader() #hỗ trợ ghi first_name và last_name vào dòng đầu tiên

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
         #csv_writer = csv.writer(new_file, delimiter='\t') 
    '''\t là dấu tab, Tham số delimiter='\t' nghĩa là thay vì ngăn cách bằng 
        dấu phẩy , mặc định, file mới sẽ ngăn cách các giá trị bằng dấu tab (\t)'''


     #   for line in csv_reader:
      #      csv_writer.writerow(line)
