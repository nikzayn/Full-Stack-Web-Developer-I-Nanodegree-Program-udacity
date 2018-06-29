import turtle

def turtle_triangle(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.left(120)

def turtle_triangle1(some_turtle1):
    for i in range(1,3):
        some_turtle1.forward(40)
        some_turtle1.left(120)

def turtle_triangle2(some_turtle2):
    for i in range(1,3):
        some_turtle2.forward(20)
        some_turtle2.right(120)

def turtle_triangle3(some_turtle3):
    for i in range(1,3):
        some_turtle3.forward(20)
        some_turtle3.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("#000")

    nik = turtle.Turtle()
    nik.shape("arrow")
    nik.color("#fff")
    nik.speed(2)
    turtle_triangle(nik)
    turtle_triangle1(nik)
    turtle_triangle2(nik)
    turtle_triangle3(nik)
    
    window.exitonclick()

draw_art()    
