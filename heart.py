import math
from turtle import *

def heart_a(n):
    return 15 * math.sin(n) ** 3

def heart_b(n):
    return (12 * math.cos(n) - 5 * math.cos(2 * n) - 2 * 
            math.cos(3 * n) - math.cos(4 * n))

speed(9999999999999999)#!اقصي سرعه
bgcolor("black")
penup()  

# رسم القلب
for i in range(1000):#!عدد المقاط بتاعه القلب
    x = heart_a(i) * 15
    y = heart_b(i) * 15
    goto(x, y)
    pendown()
    color('#f73487')

hideturtle()



done()