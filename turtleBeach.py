from turtle import *

speed(0)

move_distance = 20

# create beach
Screen().bgcolor("#D2691E")

# draw ocean
penup()
goto(100, 200)
pendown()

color("blue")

begin_fill()
goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)
end_fill()

# set turtle starting position
penup()
goto(-150, 0)
shape("turtle")
color("green")

def move_up ():
  setheading(90)
  forward(move_distance)
  check_goal()

def move_down ():
  setheading(270)
  forward(move_distance)
  check_goal()

def move_left ():
  setheading(180)
  forward(move_distance)
  check_goal()

def move_right ():
  setheading(0)
  forward(move_distance)
  check_goal()

# called when we move the turtle
def check_goal ():
  if xcor() > 100:
    hideturtle()
    color("white")
    write("YOU WIN!")

    Screen().onkey(None, "Up")
    Screen().onkey(None, "Down")
    Screen().onkey(None, "Left")
    Screen().onkey(None, "Right")

# key press events
Screen().onkey(move_up, "Up")
Screen().onkey(move_down, "Down")
Screen().onkey(move_left, "Left")
Screen().onkey(move_right, "Right")

# listen for key presses
Screen().listen()

# if you are using a local environment such as
# Visual Studio Code, add "done()" at the end
# to prevent the output window from closing 
done()