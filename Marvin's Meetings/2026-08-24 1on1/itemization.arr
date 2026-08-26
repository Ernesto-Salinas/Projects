use context starter2024

  
# Enumeration: Countably finite set of elements.
# Intervals: Element belonging to one of many infinite set of elements.

# Itemization: Enumeration + Intervals.

#Libraries
include image
include reactors

# A RocketState is one of:
# - Integer in range [0, 3]
# - "launched"

RS_0 = 0
RS_1 = 1
RS_2 = 2
RS_3 = 3
RS_LAUNCHED = "launched"

# RocketState -> ?
fun rocket-state-template(rs):
  if rs == RS_LAUNCHED: ...
  else if (rs >= RS_0) and (rs <= RS_3): ...
  end
end

# PROJECT: A rocket launch! We are going to create a
# game where there is a rocket sitting on the ground.
# When you left click, it changes to the next state. Left clicking
# on launched does nothing.
# You can see the number count on top of the rocket.
# The higher the count, the greener the text.
# The lower the count, the reder the text.
# When the count reaches 0, the text says launched, and there is
# an orange rectangle below the rocket.
# Extra Credit: Learn how to use the image library to import images.
# Make the rocket and fire images not just rectangles, but an
# actual rocket and fire image. 

fun count-down(rs):
  if rs == RS_3: RS_2
  else if rs == RS_2: RS_1
  else if rs == RS_1: RS_0
  else if rs == RS_0: RS_LAUNCHED
  end
where:
  count-down(RS_3) is RS_2
  count-down(RS_2) is RS_1
  count-down(RS_1) is RS_0
  count-down(RS_0) is RS_LAUNCHED
end



UROCKET = image-file("./images/UnlaunchedRocket.png")
LROCKET = image-file("./images/LaunchedRocket.png")
CD3 = text-font("3", 128, "red", "Gill Sans", 
        "decorative", "normal", "bold", false)
CD2 = text-font("2", 128, "orange", "Gill Sans", 
        "decorative", "normal", "bold", false)
CD1 = text-font("1", 128, "yellow", "Gill Sans", 
        "decorative", "normal", "bold", false)
CD0 = text-font("0", 128, "green", "Gill Sans", 
        "decorative", "normal", "bold", false)

#Purpose: To take in the RocketState and generate an Image.
#signature: RocketState -> Image of Rocket
fun draw-rocket(rs):
  if rs == RS_LAUNCHED:
    LROCKET
  else if (rs >= RS_0) and (rs <= RS_3):
    UROCKET
  end
where:
  draw-rocket(RS_0) is UROCKET
  draw-rocket(RS_LAUNCHED) is LROCKET
end

#Take in the RocketState, and generate the CountDown
#RocketState -> CountDown
fun draw-count-down(rs):
  if rs == RS_3: CD3
  else if rs == RS_2: CD2
  else if rs == RS_1: CD1
  else if rs == RS_0: CD0
  end
where:
  draw-count-down(RS_3) is CD3
  draw-count-down(RS_2) is CD2
  draw-count-down(RS_1) is CD1
  draw-count-down(RS_0) is CD0
end

#Take in the RocketState, and generate an image of the rocket with the correct CountDown.
# RocketState -> Image of Rocket + CountDown
fun draw-rocket-count-down(rs):
  if rs == RS_LAUNCHED:
    draw-rocket(rs)
  else if (rs >= RS_0) and (rs <= RS_3):
    overlay-align("middle", "top", 
      draw-count-down(rs), 
      draw-rocket(rs))
  end
where:
  draw-rocket-count-down(RS_3) is overlay-align(
    "middle", "top", 
    draw-count-down(RS_3), 
    draw-rocket(RS_3))
end


#Upon mouse-click, it progresses the RocketState.
#RocketState, Number, Number, MouseEvent -> RocketState
fun mouse-click-to-launch(rs, x, y, mouse-event):
  if mouse-event == "button-down": count-down(rs)
  else: rs
  end 
end
  

  
  
  
animate = reactor:
  init: RS_3,
  on-mouse: mouse-click-to-launch,
  to-draw: draw-rocket-count-down
end

#interact(animate)

# ASIDE: Wishlisting. Iterative refinement.
# How do we go from nothing to something? 
# Identifying what functions need to be written, and in what order roughly. 
# To wishlist is to write function headers (the function without body and tests) as well
# as the first two steps of the function design recipe (purpose statement and signature).
# Do this whenever you want to sketch out what all the functions generally are without having
# to spend all that time dealing with the details. This prevents you from spending lots of time
# writing functions that don't end up being used.