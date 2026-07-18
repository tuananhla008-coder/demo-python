# Thông báo khi module được import
print("Module đã được import thành công!")

# Biến thử nghiệm
test = "Chuỗi thử nghiệm"

def find_index(sequence, target):
    """
    Tìm vị trí (index) của một giá trị trong chuỗi/sequence.
    Trả về -1 nếu không tìm thấy.
    """
    for index, value in enumerate(sequence):
        if value == target:
            return index
    return -1
