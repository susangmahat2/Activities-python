import turtle
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(700,900)
polygon=turtle.Turtle()

number_sides=8
side_length=70
angle=360/number_sides
for i in range(number_sides):
    polygon.backward(side_length)
    polygon.left(angle)
turtle.done()
