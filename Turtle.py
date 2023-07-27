import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor('black')
t = turtle.Turtle()
t.speed(0)
t.color('#0afc0e')
rotate = int(360)

def draw_circles(t,size):
    for i in range(10):
        t.circle(size)
        size -= 4

def draw_special(t,size,repeat):
    for i in range(repeat):
        draw_circles(t,size)
        t.right(360/repeat)

draw_special(t,120,10)

t2 = turtle.Turtle()
t2.speed(0)
t2.color('#f50202')
rotate = int(90)

def draw_circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10

def draw_special(t,size,repeat):
    for i in range(repeat):
        draw_circles(t,size)
        t.right(360/repeat)

draw_special(t2,120,10)

t3 = turtle.Turtle()
t3.speed(0)
t3.color('#6734eb')
rotate = int(80)

def draw_circles(t,size):
    for i in range(4):
        t.circle(size)
        size -= 5

def draw_special(t,size,repeat):
    for i in range(repeat):
        draw_circles(t,size)
        t.right(360/repeat)

draw_special(t3,120,10)

t4 = turtle.Turtle()
t4.speed(0)
t4.color('#340770')
rotate = int(90)

def draw_circles(t,size):
    for i in range(4):
        t.circle(size)
        size -= 19

def draw_special(t,size,repeat):
    for i in range(repeat):
        draw_circles(t,size)
        t.right(360/repeat)

draw_special(t4,120,10)

t5 = turtle.Turtle()
t5.speed(0)
t5.color('#080000')
rotate = int(90)

def draw_circles(t,size):
    for i in range(4):
        t.circle(size)
        size-=20

def draw_special(t,size,repeat):
    for i in range(repeat):
        draw_circles(t,size)
        t.right(360/repeat)

t6 = turtle.Turtle()
t6.speed(0)
t6.color('#eb3434')
rotate = int(90)

def draw_circles(t,size):
    for i in range(4):
        t.circle(size)
        size-=20

def draw_special(t,size,repeat):
    for i in range(repeat):
        draw_circles(t,size)
        t.right(360/repeat)

draw_special(t6,120,10)
turtle.done()
