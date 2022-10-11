#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.color(turtle_colors.pop())
  my_turtles.append(t)

#  set the start location for the line of turtles
startx = 0
starty = 0
startdir = 0
length = 25

# iterate over the turtles, sending them to a location, moving them
for t in my_turtles:
  t.seth(startdir)
  t.pu()
  t.goto(startx, starty)
  t.pd()
  t.right(45)     
  t.forward(length)

#	Change variables for next turtle
  startx = t.xcor()
  starty = t.ycor()
  startdir = t.heading()
  length += 25

wn = trtl.Screen()
wn.mainloop()
