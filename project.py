import turtle
screen=turtle.Screen()
tom = turtle.Turtle()
screen.setup(500,500)
screen.bgcolor('silver')

t2 = turtle.Turtle()
tom.speed(0)
tom.pensize(2)

tom.penup()
tom.goto(-100, 50)
tom.fillcolor('blue')
tom.begin_fill()
tom.pendown()
tom.circle(50)
tom.end_fill()

t2.write("Turtle Presentation",font=("arial",24, "bold"),align="center")

tom.penup()
tom.goto(-150,-150)
tom.pendown()
screen.addshape("turtle1.gif")
tom.shape("turtle1.gif")
tom.stamp()

tom.penup()
tom.goto(120,150)
tom.pendown()
screen.addshape("swimturtle.gif")
tom.shape("swimturtle.gif")

enter = input("Continue?")


#slidetwo==================================================
tom.clear()
tom.clearstamps()
t2.clear()
t2.clearstamps()
tom.shape("classic")
screen.bgcolor('pink')
t2.penup()


t2.write("Favorite Foods",font=("arial",24, "bold"),align="center")
t2.goto(0,-50)
t2.write("1. Pizza",font=("arial",24, "bold"),align="center")
t2.goto(0,-100)
t2.write("2.Pasta",font=("arial",24, "bold"),align="center")
t2.goto(0,-150)
t2.write("3. Salad",font=("arial",24, "bold"),align="center")
t2.penup()

tom.penup()
tom.goto(-140,-140)

turtle.addshape("pizza1.gif")
tom.shape("pizza1.gif")

a = tom.stamp()

tom.penup()
tom.goto(-140,150)

turtle.addshape("pasta.gif")
tom.shape("pasta.gif")


b = tom.stamp()

tom.goto(140,140)

turtle.addshape("salad.gif")
tom.shape("salad.gif")

c = tom.stamp()

t2.goto(115,-150)
t2.fillcolor('purple')
t2.begin_fill()
t2.forward(150)
t2.left(90)
t2.forward(100)
t2.left(90)
t2.forward(150)
t2.left(90)
t2.forward(100)
t2.end_fill()

enter = input("Next Slide?")


#slidethree=-=========================================
tom.clear()
tom.clearstamps()
t2.clear()
t2.clearstamps()
tom.shape("classic")
screen.bgcolor('blue')

t2.penup()
t2.goto(0,0)
t2.write("Hobbies",font=("arial",24, "bold"),align="center")
t2.goto(0,-50)
t2.write("1. Volleyball",font=("arial",24, "bold"),align="center")
t2.goto(0,-100)
t2.write("2.Softball",font=("arial",24, "bold"),align="center")
t2.goto(0,-150)


tom.penup()
tom.goto(-140,-140)

turtle.addshape("volleyball.gif")
tom.shape("volleyball.gif")

a1 = tom.stamp()

tom.penup()
tom.goto(-140,150)

turtle.addshape("softball.gif")
tom.shape("softball.gif")

b1 = tom.stamp()


t2.penup()
t2.goto(150,150)
t2.pendown()

t2.pencolor('black')
t2.fillcolor('yellow')
t2.begin_fill()

t2.begin_fill()
t2.goto(50,50)
t2.goto(150,50)
t2.goto(150,150)
t2.end_fill()

enter = input("Continue?")

#Slidefour=====================================================================
tom.clear()
tom.clearstamps()
t2.clear()
t2.clearstamps()
tom.shape("classic")
screen.bgcolor('yellow')

t2.penup()
t2.goto(0,0)
t2.write("Favorite Movie",font=("arial",24, "bold"),align="center")
t2.goto(0,-50)
t2.write("Bad Boys",font=("arial",24, "bold"),align="center")
t2.goto(0,-100)
tom.penup()
tom.goto(-140,-140)

turtle.addshape("movie.gif")
tom.shape("movie.gif")

a2 = tom.stamp()

tom.penup()
tom.goto(140,150)

turtle.addshape("movie1.gif")
tom.shape("movie1.gif")

b2 = tom.stamp()

t2.goto(100,-100)
t2.fillcolor('green')
t2.begin_fill()
t2.forward(50)
t2.left(45)
t2.forward(50)
t2.left(45)
t2.forward(50)
t2.left(45)
t2.forward(50)
t2.left(45)
t2.forward(50)
t2.left(45)
t2.forward(50)
t2.forward(50)
t2.left(45)
t2.forward(50)
t2.left(45)
t2.end_fill()

enter = input("Continue?")

#Slidefive
tom.clear()
tom.clearstamps()
t2.clear()
t2.clearstamps()
tom.shape("classic")
screen.bgcolor('orange')

t2.penup()
t2.goto(0,0)
t2.write("Favorite Sport",font=("arial",24, "bold"),align="center")
t2.goto(0,-50)
t2.write("Volleyball",font=("arial",24, "bold"),align="center")
t2.goto(0,-100)
tom.penup()
tom.goto(-140,-140)

turtle.addshape("favsport.gif")
tom.shape("favsport.gif")

a3 = tom.stamp()

tom.penup()
tom.goto(-140,150)

turtle.addshape("favsport1.gif")
tom.shape("favsport1.gif")

b3 = tom.stamp()

t2.goto(100,-200)
t2.fillcolor('black')
t2.begin_fill()
t2.pendown()
t2.goto(200,-200)
t2.goto(180,-100)
t2.goto(120,-100)
t2.goto(100,-200)
t2.end_fill()
turtle.done()
