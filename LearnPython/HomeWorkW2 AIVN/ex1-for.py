import random

face_1 = face_2 = face_3 = face_4 = face_5 = face_6 = 0
total_plips = 10000

for i in range(total_plips):
    num = random.randint(1,6)
    if (num == 1): face_1 += 1
    elif (num == 2 ): face_2 +=1
    elif (num == 3 ): face_3 +=1
    elif (num == 4 ): face_4 +=1
    elif (num == 5 ): face_5 +=1
    else: face_6 +=1

print('Total flips:', total_plips)
print('Times are face 1:',face_1)
print('Times are face 2 :',face_2)
print('Times are face 3 :',face_3)
print('Times are face 4 :',face_4)
print('Times are face 5 :',face_5)
print('Times are face 6 :',face_6)
