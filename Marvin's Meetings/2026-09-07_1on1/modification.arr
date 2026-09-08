use context starter2024

  
# Enumeration: Countably finite set of elements.
# Intervals: Element belonging to one of many infinite set of elements.

# Itemization: Enumeration + Intervals.

#Libraries
include image
include reactors

# MODIFICATION: When the game first starts, the rocket is not moving. When the user 
# left clicks, the rocket will initiatiate countdown. After 3 seconds, the rocket 
# will physically move up. Note how the only time the user left clicks is to 
# initiate countdown.

# Start by modifying the data definition, and then modify the functions that
# operate on that data definition.



# A RocketState is one of:
# - Integer in range [-3, 0)
# - Integer from [0, inf)


# The first case represents time before launch in seconds.
# The second case represents time in the air in seconds.

RS_0 = 0
BL_1 = -1
BL_2 = -2
BL_3 = -3
AL_1 = 1
AL_4 = 4



# RocketState -> ?
fun rocket-state-template(rs):
  if (BL_3 <= rs) and (rs < RS_0): ...
  else if (RS_0 <= rs): ...
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
  if is-number(rs) and (rs >= RS_1) and (rs <= RS_3):
    rs - 1
  else if (rs == RS_0) or (rs == RS_LAUNCHED): RS_LAUNCHED
  end
where:
  count-down(RS_3) is RS_2
  count-down(RS_2) is RS_1
  count-down(RS_1) is RS_0
  count-down(RS_0) is RS_LAUNCHED
  count-down(RS_LAUNCHED) is RS_LAUNCHED
end



UROCKET = image-file("./images/UnlaunchedRocket.png")
LROCKET = image-file("./images/LaunchedRocket.png")

#To define the parameters for the countdown image.
#Number & ImageColor -> Image
fun draw-cd-image(countdown, color):
  text-font(num-to-string(countdown), 128, color, "Gill Sans", 
        "decorative", "normal", "bold", false)
end

CD3 = draw-cd-image(3, "red")
CD2 = draw-cd-image(2, "orange")
CD1 = draw-cd-image(1, "yellow")
CD0 = draw-cd-image(0, "green")

#Purpose: To take in the RocketState and generate an Image.
#signature: RocketState -> Image of Rocket
#|fun draw-rocket(rs):
  if is-number(rs) and (rs >= RS_0) and (rs <= RS_3):
    UROCKET
  else if rs == RS_LAUNCHED:
    LROCKET    
  end
where:
  draw-rocket(RS_0) is UROCKET
  draw-rocket(RS_LAUNCHED) is LROCKET
   end|#

#To set the color based on the RocketState
#Number -> Color
fun countdown-to-color(rs):
  if rs == RS_3: "red"
  else if rs == RS_2: "orange"
  else if rs == RS_1: "yellow"
  else if rs == RS_0: "green"
  else: "red"
  end
end
  

#Take in the RocketState, and generate the CountDown
#Number -> Image
fun draw-count-down(rs):
  color = countdown-to-color(rs)
  draw-cd-image(rs, color)
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
    LROCKET
  else if (rs >= RS_0) and (rs <= RS_3):
    overlay-align("middle", "top", 
      draw-count-down(rs), 
      UROCKET)
  end
where:
  draw-rocket-count-down(RS_3) is overlay-align(
    "middle", "top", 
    draw-count-down(RS_3), 
    UROCKET)
  draw-rocket-count-down(RS_LAUNCHED) is LROCKET
end


#fun after-launch(SAL):
# MOVE_UP = SAL * 30
  
  












#Upon mouse-click, it progresses the RocketState.
#RocketState, Number, Number, MouseEvent -> RocketState
fun mouse-click-to-launch(rs, x, y, mouse-event):
  if mouse-event == "button-down": count-down(rs)
  else: rs
  end 
end
  

#on-mouse should change by adding a line where the state changes every second after the mouse click.

#For to-draw, the function it is calling will change to accomodate the new data definition.

# on-tick

# HINTS:
# 1. A piece of info in tthe problem statetment is not being represented in the current
#    RocketState
# 2. Right now RockState is just an interval, it's dealing with numbers only.
#    Do not hestitate to introduce a string. When you have data where you don't need
#    to perform arithmetic on, string could be better.
  
animate = reactor:
    init: BL_3,
  on-mouse: mouse-click-to-launch,
  to-draw: draw-rocket-count-down
end

interact(animate)

# ASIDE: Wishlisting. Iterative refinement.
# How do we go from nothing to something? 
# Identifying what functions need to be written, and in what order roughly. 
# To wishlist is to write function headers (the function without body and tests) as well
# as the first two steps of the function design recipe (purpose statement and signature).
# Do this whenever you want to sketch out what all the functions generally are without having
# to spend all that time dealing with the details. This prevents you from spending lots of time
# writing functions that don't end up being used.


