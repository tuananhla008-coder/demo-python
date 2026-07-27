#Có 2 thuật ngữ ngày giờ chính là 'naive' và 'aware'
#Ngày giờ 'naive' không đủ thông tin để xác định những thứ như múi giờ hoặc giờ tiết kiệm chiếu sáng ban ngày
#Còn nếu muốn chi tiết hơn thì sử dụng ngày giờ 'aware'
#làm việc với ngày, tháng, năm
'''import datetime
d = datetime.date(2026, 7, 26)
print(d)
tday = datetime.date.today() #cách in ra ngày giờ địa phương hiện tại
print(tday)
print(tday.day)# nếu chỉ muốn lấy ngày
print(tday.year)# nếu chỉ muốn lấy năm
print(tday.weekday())#nếu muốn lấy ngày trong tuần thì thứ 2 là 0, chủ nhật là 6
print(tday.isoweekday())#nếu muốn lấy ngày trong tuần theo chuẩn iso thì thứ 2 là 1, chủ nhật là 7
#các phép toán trên ngày hoặc giờ
tdelta = datetime.timedelta(days=7) #sự chênh lệch thời gian bằng ngày
print(tday + tdelta) #in ra ngày tháng sau 1 tuần 
# cộng hoặc trừ 1 ngày từ 1 ngày khác làm kết quả 
# VD: ngày 2 = ngày 1 + khoảng thời gian
# VD2: ngày 1 = ngày 2 - khoảng thời gian
bday = datetime.date(2027, 7, 21)
till_bday = bday - tday
print(till_bday.days) #nếu chỉ muốn lấy số ngày thì thêm days
print(till_bday.total_seconds())#nếu chỉ muốn tính bằng giây'''

#Làm việc với ngày giờ
#import datetime
#t = datetime.time(16, 14, 21, 100000) #giờ, phút, giây, micro giây
#print(t.hour) #in giờ
# nếu muốn ưu tiên dùng tất cả ngày, tháng, năm, giờ , phút, giây thì sử dụng
'''dt = datetime.datetime(2026, 7, 26, 16, 18, 21, 100000)
print(dt.date())#lấy ngày mà không cần giờ
print(dt.time())#lấy giờ mà không cần ngày
# và đối với hàm này vẫn lấy được thuộc tính riêng lẻ như year, days, hour, ...
tdelta = datetime.timedelta(hours=7)
print(dt + tdelta)'''
'''import datetime
#hàm tạo thay thế đi kèm với ngày giờ
dt_today = datetime.datetime.today() #trả về giờ địa phương với múi giờ là none
dt_now = datetime.datetime.now()#truyền vào múi giờ
dt_utcnow = datetime.datetime.utcnow()#trả về thời gian utc hiện tại nhưng thông tin múi giờ vẫn là none
print(dt_today)
print(dt_now)
print(dt_utcnow)'''
import datetime
import pytz
#dt = datetime.datetime(2026, 7, 27, 22, 9, 21, tzinfo=pytz.UTC)
#print(dt)
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
dt_vna = dt_utcnow.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
#print(dt_vna)
print(dt_vna.strftime('%B %d, %Y')) #in từ số sang chữ-strftime
dt_str = 'July 27, 2026'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y') #in từ chữ sang số - strptime
#tra cứu các kí hiệu ở strftime.org
print(dt)
'''import pytz
print(pytz.all_timezones)  # in ra toàn bộ danh sách tên hợp lệ
for tz in pytz.all_timezones:
    if 'Asia' in tz:
        print(tz)  #lọc riêng theo từ khóa '''
