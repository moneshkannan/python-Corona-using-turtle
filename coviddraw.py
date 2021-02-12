import turtle;
t=turtle.Turtle();
s=turtle.Screen();
s.bgcolor('black')
t.pencolor('blue')
a=0
b=0
#c=0
#d=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    #t.left(c)
    #t.backward(d)
    a+=3
    b+=1
    #c+=2
    #d+=4
    if b == 210:
        break
    t.hideturtle()
t.bye()
t.done()