use context starter2024
# SITUATION: We have a electronic door, that is either open or close. Write two functions:
# 1. activate. If the door is open, close it. If it's closed, open it.
# 2. draw the electronic door. Opened should look opened. Closed should look closed.

# FOLLOW THE DESIGN RECIPE FOR DATA DEFINITION AND FUNCTION. TTHEY ARE AT THE TOP OF THIS FILE.
# Once you have two functions, apply the abstraction process to the two functions to arrive at the template.
--------------------------------------------------------


#Input Type: Door Position
#Output Type: Completed Door Operation


#Purpose: Take in the current position of the electronic door, and return the completed door operation based on the original position of the door.


POS_CLOSED = "closed"


# Template
fun door-operation-template(position):
  if not(position == POS_CLOSED):
    ...
  else if position == POS_CLOSED:
    ...
  end
end

#This function takes the current position of the door, and returns the completed operation based on entered position.
fun activate(position):
  if not(position == POS_CLOSED):
    "door has been closed"
  else if position == POS_CLOSED:
    "door has been opened"
  end
where:
  activate("closed") is "door has been opened"
  activate("wide-open") is "door has been closed"
  activate("ajar") is "door has been closed"
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
  if not(position == POS_CLOSED):
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