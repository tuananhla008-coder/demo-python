import requests

r = requests.get('https://xkcd.com/353/')

print(type(r))          # <class 'requests.models.Response'>
print(r.ok)              # True hoặc False — do SERVER quyết định
print(r.status_code)     # 200, 404... — do SERVER quyết định
print(r.text[:100])      # 100 ký tự đầu của trang HTML thật, do SERVER trả về

#download images
img_url = 'https://imgs.xkcd.com/comics/python.png'
r = requests.get(img_url)
with open('anh1.png', 'wb') as f:
    f.write(r.content)
payload = {'username': 'corey', 'password': 'testing'}

r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
#JSON
'''JSON là 1 chuỗi văn bản thuần túy (giống nội dung file .txt), còn dict Python là 1 cấu trúc dữ liệu sống trong bộ nhớ mà 
Python hiểu và thao tác được trực tiếp (payload['username'], thêm/xoá key...). JSON thì không — nó chỉ là chữ, muốn thao tác 
phải chuyển nó thành dict trước.'''

#Serialization
'''Serialization = quá trình chuyển đổi 1 cấu trúc dữ liệu sống trong bộ nhớ (VD dict Python) thành 
1 chuỗi văn bản để có thể lưu file hoặc gửi qua mạng.'''
#vd:
import json
pay = {'username': 'cu', 'age': '21' }
print(type(pay))
chuoi_json = json.dumps(pay)
print(chuoi_json)
print(type(chuoi_json))
'''
payl — là dict, sống trong bộ nhớ Python
json.dumps(pay) — hàm "dump string", chuyển dict thành str theo đúng cú pháp JSON
Sau khi chuyển, chuoi_json không còn là dict nữa — nó chỉ là 1 chuỗi ký tự dài, 
trông giống dict nhưng bản chất khác hẳn (không 
thể gọi chuoi_json['username'] được, vì đó là str, không phải dict)
'''

#Deserialization
'''Deserialization = quá trình ngược lại — nhận 1 chuỗi JSON (từ server, hoặc từ file), 
biến nó trở lại thành dict/list để Python thao tác được.'''
#vd:
chuoi_json = '{"username": "cu", "age": "21"}' #lưu ý khi chuyển từ json về dict bắt buộc phải có dấu '...' (hoặc "...") ở ngoài cùng, còn bên trong dùng dấu " cho đúng chuẩn JSON.
data = json.loads(chuoi_json)
print(data)
print(data['age'])
'''json.loads(...) — hàm "load string", chuyển str (JSON) ngược lại thành dict

Khi dùng requests, bạn không cần tự gọi json.loads() — thư viện đã làm sẵn cho bạn qua phương thức:

python
data = r.json()

r.json() chính là gọi json.loads(r.text) phía sau, 
chỉ là requests đóng gói gọn lại thành 1 lệnh cho tiện.'''

#Đọc json từ API thật
r = requests.get('https://httpbin.org/get')
try:
    data = r.json()
    print(data)
except requests.exceptions.JSONDecodeError:
    print('Server không trả về JSON hợp lệ, có thể đang lỗi/quá tải')
### Nhóm A — Thuộc tính (attributes) của `Response`, không có `()`
'''
| Tên            | Kiểu dữ liệu | Ý nghĩa                                                        |
|----------------|--------------|-----------------------------------------------------------------|
| `r.text`       | `str`        | Nội dung trả về dạng văn bản                                    |
| `r.content`    | `bytes`      | Nội dung trả về dạng nhị phân thô                                |
| `r.status_code`| `int`        | Mã trạng thái HTTP, VD `200`, `404`                              |
| `r.ok`         | `bool`       | `True` nếu status từ 200-399                                     |
| `r.reason`     | `str`        | Mô tả ngắn cho status_code, VD `'OK'`, `'Not Found'`             |
| `r.headers`    | `dict`-like  | Thông tin kỹ thuật server trả về                                 |
| `r.url`        | `str`        | URL thực tế cuối cùng được gọi                                   |
| `r.encoding`   | `str`        | Kiểu mã hóa ký tự, VD `'utf-8'`                                  |
| `r.cookies`    | object riêng | Cookie server gửi kèm                                            |
| `r.elapsed`    | `timedelta`  | Thời gian request mất bao lâu để hoàn thành                      |
| `r.history`    | `list`       | Danh sách các request trung gian nếu bị chuyển hướng (redirect)  |
| `r.request`    | object riêng | Thông tin về chính request đã gửi đi (URL, headers, body...)     |
'''
### Nhóm B — Phương thức (methods) của `Response`, bắt buộc có `()`
'''
| Tên                              | Ý nghĩa                                                                       |
|-----------------------------------|--------------------------------------------------------------------------------|
| `r.json()`                        | Chuyển `r.text` thành `dict`/`list`, báo lỗi nếu không đúng cú pháp JSON       |
| `r.raise_for_status()`            | Nếu status lỗi (4xx/5xx), tự động ném exception; nếu ổn thì không làm gì       |
| `r.iter_content(chunk_size=...)`  | Duyệt qua nội dung theo từng phần nhỏ — dùng khi tải file lớn                  |
| `r.close()`                       | Đóng kết nối, giải phóng tài nguyên (thường không cần gọi tay, tự động xử lý)  |
'''
#Authentication (Xác thực đăng nhập)
#Nhiều API yêu cầu bạn chứng minh mình có quyền truy cập trước khi trả dữ liệu — giống như phải đăng nhập trước khi xem trang cá nhân trên 1 website.
#Basic Auth
from requests.auth import HTTPBasicAuth
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=HTTPBasicAuth('cuuuu', 'tuananh'))
print(r.text)
#Kiểm tra xác thực thành công hay không
if r.status_code == 200:
    print('Đăng nhập thành công')
elif r.status_code == 401:
    print('Sai thông tin đăng nhập')

#Headers tuỳ chỉnh
headers = {'Authorization': 'token day_la_token_cua_ban'}

r = requests.get('https://api.github.com/user', headers=headers)   
# Danh sách lỗi/tình huống tương tự cần lưu ý khi làm việc với requests
'''
| Tình huống                         | Dấu hiệu                                         | Có crash không                                                                 |
|------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------------|
| Server quá tải/bảo trì              | status_code = 503                                | Không crash nếu chỉ dùng `.text`; crash nếu dùng `.json()` trên nội dung không phải JSON |
| Không tìm thấy tài nguyên           | status_code = 404                                | Không crash — chỉ cần bạn tự kiểm tra `if r.ok`                                |
| Sai xác thực                        | status_code = 401 (Unauthorized) hoặc 403 (Forbidden) | Không crash                                                                   |
| Gọi quá nhiều request liên tục      | status_code = 429 (Too Many Requests)            | Không crash                                                                   |
| Lỗi phía server                     | status_code = 500 (Internal Server Error)        | Không crash nếu chỉ đọc `.text`                                               |
| Mất mạng / không kết nối được       | Ném ra requests.exceptions.ConnectionError       | Crash nếu không có `try/except`                                               |
| Server phản hồi quá chậm            | Ném ra requests.exceptions.Timeout (nếu có set timeout=) | Crash nếu không có `try/except`                                         |
| Gọi `.json()` trên nội dung không phải JSON | Ném ra requests.exceptions.JSONDecodeError | Crash nếu không có `try/except` (đúng lỗi bạn vừa gặp)                        |
'''