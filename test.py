# # print("Assalomu alaykum")
# # print("salom") # izoh:
# # print("hello guys")
# # print("""men \"noutbook\" sotib oldim
# # va undan foydalanyapman""")
# # print("Odami ersang demagin odami, \nOnikin yoq \nxalq g`ami")
# # print(16/4)
# # print(16//4)
# # print(5**3)
# print("Beshning kvadrati", 5**2, "ga teng")
# # print("3x3=",3*3)


# import turtle
# turtle.bgcolor("black")
# turtle.speed(0)
# turtle.hideturtle()

# Colors=["yellow", "red", "yellow", "red"]

# for i in range(120):
#     for c in Colors:
#         turtle.color(c)
#         turtle.circle(200-i, 100)
#         turtle.lt(90)
#         turtle.circle(200-i, 100)
#         turtle.rt(60)
#         turtle.end_fill()

# turtle.mainloop()

from asyncore import write
import turtle

turtle.Screen().bgcolor("black")

t=turtle.Turtle()
t.speed(10)
t.pensize(10)
t.penup()

def draw_circle():
    t.setposition(0,-280)
    t.pendown()
    t.begin_fill()
    t.color('red')
    t.pencolor("white")
    t.circle(300)
    t.end_fill()
    t.penup()

def draw_circle2():
    t.pensize(2)
    t.setposition(0,-230)
    t.pendown()
    t.begin_fill()
    t.color('black')
    t.circle(250)
    t.end_fill()
    t.penup()

def draw_A():
    t.setposition(30,-110)
    t.pendown()
    t.begin_fill()
    t.color('red')
    t.pensize(10)
    t.pencolor("white")
    t.forward(23)
    t.backward(123)
    t.left(60)
    t.backward(220)
    t.right(60)
    t.backward(100)
    t.right(117)
    t.backward(710)
    t.right(63)
    t.backward(110)
    t.right(90)
    t.backward(510)
    t.right(90)
    t.backward(100)
    t.right(90)
    t.backward(70)
    t.end_fill()
    t.penup()

def draw_triangle():
    t.pensize(10)
    t.setposition(53,-40)
    t.pendown()
    t.begin_fill()
    t.color("black")
    t.pencolor("white")
    t.right(90)
    t.forward(100)
    t.right(115)
    t.forward(250)
    t.right(157)
    t.forward(227)
    t.end_fill()

def draw_arrow():
    t.backward(80)
    t.left(42)
    t.forward(147)
    t.right(83)
    t.forward(140)

draw_circle()
draw_circle2()
draw_A()
draw_triangle()
draw_arrow()

t.hideturtle()
turtle.done()
