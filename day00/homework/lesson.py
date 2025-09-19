from turtle import *
speed(10)
shape("turtle")
speed(5)
width(7)
color("black") 
forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()





penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

exitonclick


#drawing a window

penup()
goto(20,50)
pendown()
color("brown")

right(240)
forward(30)
left(90)
forward(70)
left(90)
forward(30)
left(90)
forward(70)
left(90)
forward(15)
left(90)
forward(70)
penup()
goto(35,85)
pendown()
right(90)
forward(15)
right(180)
forward(30)

left(90)
forward(35)
left(90)
penup()
goto(35,50)
forward(120)
penup()
pendown()
left(90)
forward(70)
left(90)
left(180)
forward(30)
left(90)
left(180)
forward(70)
left(90)
left(180)
forward(30)
left(90)
left(180)
forward(35)
left(90)
left(180)
forward(30)
left(90)
right(90)
left(90)
forward(35)
left(90)
forward(15)
left(90)
forward(70)

exitonclick()
