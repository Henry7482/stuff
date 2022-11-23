import turtle
#set up
win = turtle.Screen()
tiro = turtle.Turtle()
win.bgcolor("red")
tiro.color("red")

#draw
def draw(num, len):
    tiro.color("yellow")
    tiro.begin_fill()
    for i in range(num):
        tiro.forward(len)
        tiro.right(360/num)
    tiro.end_fill()
    win.exitonclick()

#main
n = int(input("number"))
l = int(input("length"))

#center
win.setup(500, 500)
tiro.setx(-(l/2))
tiro.sety(l/2)

draw(n, l)


