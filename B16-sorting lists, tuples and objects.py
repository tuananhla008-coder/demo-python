li = [9, 5, 3, 6, 8, 1, 7, 2, 4]
s_li = sorted(li, reverse = True)  #reverse = True biểu thi cho sắp xếp giảm dần
#nếu thay bằng li.sort() thì giá trị sẽ trả về none
print('Sắp xếp:\t', s_li)
li.sort()
print('Hàm gốc:\t', li)
'''hàm sorted() và phương thức sort() là hàm sorted() sẽ trả về 1 danh sách
được sắp xếp mới nhưng phương thức sort() chỉ sắp xếp danh sách tại chỗ và sau đó 
trả về none '''
#NÊN ƯU TIÊN SỬ DỤNG HÀM SORTED() HƠN BỞI VÌ SẼ KHÔNG BỊ GIỚI HẠN NHƯ PHƯƠNG THỨC SORT()
tup = (2, 4, 6, 9, 7, 5, 8, 3, 1)
s_tup = sorted(tup, reverse = True)
print('Tuple:\t', s_tup)
di = {'name': 'Corey', 'job': 'programing', 'age': '21', 'os': 'Aspire'}
s_di = sorted(di)
print('Dic:\t', s_di) #trả về các khóa keys