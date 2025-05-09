import turtle
t=turtle.Turtle()
t.screen.bgcolor("white")
t.pensize(3)
t.color=("brown")
t.left(90)
t.backward(80)
t.speed(0)
t.shape("triangle")
def tree(i):
    if i<15:
        return
    else:
        t.forward(i)
        t.color("hotpink")
        t.circle(4)
        t.color("aqua")
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
        tree(90)
turtle.done()