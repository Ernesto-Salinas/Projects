use context starter2024
include reactors

# Information <---> Data

# Design Recipe
# Design: Going from A to B systematically.
# Recipe: A series of steps you can follow. 

# Data Definition Design Recipe
# Data definition defines the relationship between some information and its corresponding data representation.
# Data Representation: How the computer encodes a piece of information. E.g. Number, Boolean, String, Image...
# Interpretation: What does the representation actually mean?
# In summary, how the computer understands VS how the human understands.

# 1. What is the data representation? - For computer.
# 2. What is the interpretation? - For human.
# 3. What are examples of this data definition.
# 4. What is the template? - The bridge between the data representation and functions that operate on it.

# A Temperature is a Number.
# INTERPRETATION: The temperature, in degree Fahrenheit. 

T_3F = 3
T_20F = 20
T_32F = 32   # Where water freezes
T_N5F = -5
T_N40F = -40
T_5_4F = 5.4
T_1_OVER_3F = 1/3
T_1F = 1
T_0F = 0

# Function Design Recipe

# 1. Signature of the function. What's the input and output types?
#    - How the computer understands the function.
# 2. Purpose statement - What is the purpose of this function?
#    - How the human understands it.
# 3. Write in the stub, and then Examples/Tests.
# 4. Write the body of the function

# TASK: Convert temperature from Fahrenheit to Celsius.

# Temperature -> Number
# Gets the Celsius of the given Fahrenheit temperature.
fun fahrenheit-to-celsius(f):
  (f - 32) * 5/9
where:
  fahrenheit-to-celsius(T_0F) is (-32 * 5/9)
  fahrenheit-to-celsius(T_N5F) is (-37 * 5/9)
  fahrenheit-to-celsius(T_32F) is 0
  fahrenheit-to-celsius(T_N40F) is -40
end


#|
Notes left for me in prior 1on1:

Enumeration

Encoding information where it can be one of many things.

A TrafficLight is one of:
- "red"
- "yellow"
- "green"
   "A traffic light is a light that has red, yellow, and green which represent when you need to stop, go, and when it will become red shortly at an intersection."
Design Recipe 

|#

TOP = "red"
MID = "yellow"
BOT = "green"

# TrafficLight -> ?
fun traffic-light-template(traffic_light):
  if traffic_light == TOP:      ...
  else if traffic_light == MID: ...
  else if traffic_light == BOT: ...
  end
end


# OBSERVATIONS:
# - A reason for using constants for examples is so that
#   we get help from the programming language when we typo.
# - If we decide to change the underlying data representation, we only need to change one or two lines, rather than locate all the strings in the entire codebase.
# - For enumeration specifically, there's a finite set of elements for that data definition. Always exhaust that finite set. List every single possible value for that data definition.


# TASK: Design a function, rotate-traffic-light, that makes green become yellow, yellow become red, red becomes green.
# TrafficLight -> TrafficLight
# Traffic lights cycle through 3 different colors. We want to capture that cycle in this function.
fun rotate-traffic-light(traffic_light):
  if traffic_light == TOP: BOT
  else if traffic_light == MID: TOP
  else if traffic_light == BOT: MID
  end
where:
  rotate-traffic-light(TOP) is BOT
  rotate-traffic-light(MID) is TOP
  rotate-traffic-light(BOT) is MID
end

# Difference between else if ... VS else on the last condition in if-expression.
# - Addition of more cases to the enumeration. It's the difference between getting an exception or the wrong value. E.g. OCaml.
# - else if... mirrors the data definition.


# The structure of the function follows the structure of the data definition.

# HW if you have time:
# Design a function traffic-light-to-image, then produces the corresponding traffic light image for the given trafflic light.

# HW if you have time:
# Design a function traffic-light-to-image, then produces the corresponding traffic light image for the given trafflic light.




# To generate a traffic light based on the desired color.
fun traffic-light-highlight(color, red-fill, yellow-fill, green-fill):
  red-light = above(
    circle(30, red-fill, "red"),
    square(15, 0, "white"))
  yellow-light = above(
    circle(30, yellow-fill, "yellow"),
    square(15, 0, "white"))
  green-light = circle(30, green-fill, "green")
  three-lights = above(
    above(
      red-light, 
      yellow-light), 
    green-light)
  overlay-xy(
    three-lights,
    -15, -15,
    rectangle(90, 240, "solid", "black"))
end


fun draw-traffic-light(traffic_light):
  if traffic_light == TOP:      traffic-light-highlight(TOP, "solid", 0.2, 0.2)
  else if traffic_light == MID: traffic-light-highlight(MID, 0.2, "solid", 0.2)
  else if traffic_light == BOT: traffic-light-highlight(BOT, 0.2, 0.2, "solid")
  end
where:

  draw-traffic-light("red") is traffic-light-highlight(TOP, "solid", 0.2, 0.2)
  draw-traffic-light("yellow") is traffic-light-highlight(MID, 0.2, "solid", 0.2)
  draw-traffic-light("green") is traffic-light-highlight(BOT, 0.2, 0.2, "solid")
end



draw-traffic-light("red")
draw-traffic-light("yellow")
draw-traffic-light("green")

# TrafficLight, number, number, KeyEvent -> TrafficLight
fun mouse-click-through-lights(traffic_light, x, y, key-event):
  if key-event == "button-down":
    rotate-traffic-light(traffic_light)
  else:
    traffic_light
  end
end


animate = reactor:
  init: TOP,
  on-mouse: mouse-click-through-lights,
  to-draw: draw-traffic-light
end

interact(animate)





# Abstraction recipe (rough draft)
# 1. Identify similarities and differences.
# 2. Replace the differences with ...s.
# 3. Convert each ... to a parameter.
# 4. Rename the function to something descriptive, and give the function a purpose statement.
# 5. Replace the original instances of repeated code with the abstraction.



# SITUATION: We have a electronic door, that is either open or close. Write two functions:
# 1. activate. If the door is open, close it. If it's closed, open it.
# 2. draw the electronic door. Opened should look opened. Closed should look closed.

# FOLLOW THE DESIGN RECIPE FOR DATA DEFINITION AND FUNCTION. TTHEY ARE AT THE TOP OF THIS FILE.
# Once you have two functions, apply the abstraction process to the two functions to arrive at the template. 


#Input Type: Door Position
#Output Type: Completed Door Operation


#Purpose: Take in the current position of the electronic door, and return the completed door operation based on the original position of the door.

#|
-- Data Definitions--
A Door is one of:
-"open"
-"closed"
|#




POS_CLOSED = "closed"
POS_OPEN = "open"


# Template
fun door-operation-template(position):
  if position == POS_OPEN:
    ...
  else if position == POS_CLOSED:
    ...
  end
end

#Signature:
# Door -> Door

#This function takes the current position of the door, and returns the completed operation based on entered position.
fun activate(position):
  if position == POS_OPEN:
    POS_CLOSED
  else if position == POS_CLOSED:
    POS_OPEN
  end
where:
  activate("closed") is POS_OPEN
  activate("open") is POS_CLOSED
  
end

#This function draws the brown door with golden door knob.
fun draw-door():
  rec1-2 = beside(rectangle(50, 150, "outline", "black"), rectangle(50,150,0,"brown"))
  rec1-2-3 = beside(rec1-2, rectangle(50, 150, "outline", "black"))
  rec-top-mid = above(rec1-2-3, square(150, 0, "brown"))
  int-door = above(rec-top-mid, rec1-2-3)
  doorknob = overlay(circle(12, "outline", "black"), circle(12, "solid", "gold"))
  doorknob-int-door = beside(doorknob, int-door)
  door = place-image(
    doorknob-int-door, 
    113, 275,
    rectangle(250, 550, "solid", "brown"))
  door  
end

#This function draws the white door frame.
fun draw-door-frame():
  left-df = rectangle(30, 580, "solid", "white")
  left-top-df = overlay-align(
    "left", "top",
    left-df,
    rectangle(310, 30, "solid", "white"))
  door-frame = overlay-align(
    "right", "top",
    left-top-df,
    rectangle(30, 580, "solid", "white"))
  door-frame
end

# The function takes the current position of the door, and then draws the door after the operation has been completed.
fun draw-door-operation(position):
  if position == POS_OPEN:
    overlay-xy(
      draw-door(),
      -30, -30,
      draw-door-frame())
  else if position == POS_CLOSED:
    overlay-xy(
      flip-horizontal(draw-door()),
      -280, -30,
      draw-door-frame())
  end
end

draw-door-operation("closed")
draw-door-operation("open")


# Door Number Number KeyEvent -> Door
fun on-mouse-door(door, x, y, key-event):
  if key-event == "button-down":
    activate(door)
  else:
    door
  end
end

# I am going to make a GUI app where we can open
# and close our door.
# It has a model/state. 
anim = reactor:
  init: POS_CLOSED,
  on-mouse: on-mouse-door,
  to-draw: draw-door-operation
end

interact(anim)

# RECAP

# 1. reactor: ... end
# 2. init: ..., on-mouse: ..., to-draw: ...
# 3. init: POS_CLOSED
# 4. on-mouse: on-mouse-door (and I implemented that too)
# 5. to-draw: draw-door-operation
# 6. anim = reactor: ... end
# 7. interact(anim)