#vòng lặp for và while
nums = [1, 2, 3, 4, 5]
for num in nums: 
    print(num)
#break - khi muốn lặp đến số chỉ định và thoát khỏi vòng lặp
nums = [1, 2, 3, 4, 5]
for num in nums: 
    if num == 3:
        break
    print(num)    
#continue - nếu chỉ muốn mất 1 gái trị nhưng vẫn trong vòng lặp
nums = [1, 2, 3, 4, 5]
for num in nums: 
    if num == 3:
        continue
    print(num) 
# vòng lặp trong vòng lặp   
nums = [1, 2, 3, 4, 5]
for num in nums:
    for str in 'abc':
        print(str, num) 
#chỉ chạy số vòng lặp nhất định
for i in range(1, 10, 2): #1 là start; 10 là stop; 2 là step
    print(i)
#vòng lặp while
x = 10
while x > 1:
    if x == 7:
        break
    print(x)
    x -= 1     
