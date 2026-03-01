import turtle
mywn=turtle.Screen()
mywn.bgcolor("Red")
mywn=turtle.title("turtle")
mypen=turtle.Turtle()
size=0
while True:
    for i in range(4):
        mypen.color("Purple")
        mypen.forward(size+1)
        mypen.left(90)
        size=size-5
        size=size+1
turtle.done()  
