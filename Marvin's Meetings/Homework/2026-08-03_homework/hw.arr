use context starter2024
# HW if you have time:
# Design a function traffic-light-to-image, then produces the corresponding traffic light image for the given trafflic light.

# To generate a traffic light based on the desired color.
fun traffic-light-highlight(color, red-fill, yellow-fill, green-fill):
    above(
        above(
      circle(30, red-fill, "red"), 
      circle(30, yellow-fill, "yellow")), 
    circle(30, green-fill, "green"))
end


fun traffic_light(color):
  if color == "red":
    traffic-light-highlight("red", "solid", "outline", "outline")
  else if color == "yellow":
    traffic-light-highlight("yellow", "outline", "solid", "outline")
  else if color == "green":
    traffic-light-highlight("green", "outline", "outline", "solid")
  end
where:
  traffic_light("red") is circle(30, "solid", "red") and circle(30, "outline", "yellow") and circle(30,"outline", "green")
  traffic_light("yellow") is circle(30, "outline", "red") and circle(30, "solid", "yellow") and circle(30,"outline", "green")
    traffic_light("green") is circle(30, "outline", "red") and circle(30, "outline", "yellow") and circle(30,"solid", "green")
end

traffic_light("red")
traffic_light("yellow")
traffic_light("green")




# Abstraction recipe (rough draft)
# 1. Identify similarities and differences.
# 2. Replace the differences with ...s.
# 3. Convert each ... to a parameter.
# 4. Rename the function to something descriptive, and give the function a purpose statement.
# 5. Replace the original instances of repeated code with the abstraction.