#set circle's radius is R
#circle's area is PI*R*R
#Minimum Bounding Rectangle's area is 4*R*R
#so PI = circle's area/Rectangle's area * 4
import random  

x = 0
y = 0
circle_cnt = 0
point_set_num = 100000000

for i in range(point_set_num):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    
    if (x**2 + y**2)**0.5 <= 1:
        circle_cnt += 1
    
    if i % 1000000 == 0:
        print("===>{}".format(i))
print("PI's value is: {}.".format(circle_cnt/point_set_num*4))  #result is 3.14159268
