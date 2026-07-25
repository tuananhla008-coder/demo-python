import csv
html_output = ''
names = []
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data) #loại bỏ 2 dòng đầu tiên của file patrons.csv
    next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward':
            continue
        #print(line)
        names.append(f'{line[0]} {line[1]}') #line[0] là first name, line[1] là last name

#for name in names:
#    print(name)   

html_output += f'<p>Đây sẽ là danh sách {len(names)} người để bạn biết ai là người ủng hộ Corey </p>'     
html_output += '\n<ul>' #các thẻ p,ul,li là các thẻ dành cho viết đoạn code của html
#\n là xuống dòng, \t là khoảng trắng
for name in names:
    html_output += f'\n\t<li>{name}</li>' 

html_output += '\n</ul>'    
print(html_output)    