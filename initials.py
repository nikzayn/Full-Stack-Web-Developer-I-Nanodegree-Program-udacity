import turtle

def turtle_name():
    window = turtle.Screen()
    window.bgcolor("#000")

    nik = turtle.Turtle()
    nik.shape("arrow")
    nik.color("#fff")
    nik.speed(4)

    nik.left(90)
    nik.forward(200)
    nik.right(150)
    nik.forward(230)
    nik.left(150)
    nik.forward(200)

    nik.penup()
    nik.goto(250,0)

    nik.pendown()
    nik.right(20)
    nik.forward(200)
    nik.right(180)
    nik.forward(200)
    nik.right(140)
    nik.forward(200)
    

    window.exitonclick()

turtle_name()
    
