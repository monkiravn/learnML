# aivietnam.ai
import random

# Tổng số lần búng đồng xu
total_flips = 0  

# số lần mặt sau xuất hiện
num_tails = 0

# số lần mặt trước xuất hiện
num_heads = 0

for _ in range(1000):
    # sinh số ngẫu nhiên nằm trong khoảng [0,1)
    n = random.random()
    if n < 0.3:
        num_tails = num_tails + 1
    else:
        num_heads = num_heads + 1
    
    # code ở vị trí này không thuộc khối else    
    total_flips = total_flips + 1
    
# code ở ví trị này không thuộc khối code cho for
# vòng lặp for đã thực hiên xong
print('total_flips: %d' % total_flips)
print('num_tails: %d' % num_tails)
print('num_heads: %d' % num_heads)
