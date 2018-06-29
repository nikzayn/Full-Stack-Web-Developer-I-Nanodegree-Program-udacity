import turtle

def draw_rhombus(some_rhombus):
    for i in range(1,3):
        some_rhombus.forward(100)
        some_rhombus.left(45)
        some_rhombus.forward(100)
        some_rhombus.left(135)

def draw_line(some_line):
    for i in range(1,2):
        some_line.right(90)
        some_line.forward(300)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("#000")
    nik = turtle.Turtle()
    nik.speed(40)
    nik.shape("turtle")
    nik.color("#fff")
    for i in range(1,37):
        draw_rhombus(nik)
        nik.right(10)
    for i in range(37,38):
        draw_line(nik)

    window.exitonclick()

draw_art()    
