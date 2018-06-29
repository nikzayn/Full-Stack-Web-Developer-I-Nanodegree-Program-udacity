import turtle

def draw_squares(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    nik = turtle.Turtle()
    nik.shape("turtle")
    nik.color("white")
    nik.speed(2)
    for i in range(1,37):
        draw_squares(nik)
        nik.right(10)

    window.exitonclick()
    
draw_art()
