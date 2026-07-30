use context starter2024
#|Link for exercises:
https://htdp.org/2026-5-28//Book/part_one.html#%28counter._%28exercise._fun0%29%29

   NOTE: The exercises are not specifically designed for Pyret, so the referenced examples may not be helpful

Documentation:
   https://pyret.org/docs/latest/ |#

"Exercise 11"
# Define a function that consumes two numbers, x and y, and that computes the distance of point (x,y) to the origin.
fun distance(x,y):
  a2 = x * x
  b2 = y * y
  c2 = a2 + b2
  c = num-sqrt(c2)
  c
where:
  distance(12,8) is-roughly 14.4222
end

"attempt 2"
fun distance2(x,y):
  num-sqrt((x * x) + (y * y))
end

distance2(12,8)



"Exercise 12"
# An equilateral cube is a three-dimensional container bounded by six squares. You can determine the surface of a cube if you know that the square's area is its length multiplied by itself. Its volume is the length multiplied with the area of one of its squares.
fun cvolume(len):
  len * len * len
where:
  cvolume(4) is 64
end


"Exercise 13"
# Define the function string-first, which extracts the first 1String from a non-empty string.
fun string-first(string):
  if is-string(string):
    if string <> "":
      string-substring(string, 0, 1)
    else:
      "Please enter a string."
    end
  else:
    "Please enter a string."
  end
end


string-first("Hello")
string-first(7)
string-first("")

"Exercise 14"
# Define the function string-last, which extracts the last 1String from a non-empty string.
fun string-last(string):
  if is-string(string):
    if string <> "":
      string-substring(string, string-length(string) - 1, string-length(string))
    else:
      "Please enter a string."
    end
  else:
    "Please enter a string."
  end
end

string-last("How are you")
string-last(7)
string-last("")

"Exercise 15"
# Define ==>. The function consumes two Boolean values, call them sunny and friday. Its answer is #true if sunny is false or friday is true. Note Logicians call this Boolean operation implication, and they use the notation sunny => friday for this purpose.

# 7/20/26 Meeting - We went throughh Exercise 15 together, and he helped me understand Booleans, and how to check functions using "Where:" within a function, and "Check" 
fun implies(sunny, friday):
  not(sunny) or friday
   
where:
    implies(false, true) is true
    implies(true, true) is true
    implies(true, false) is false
    implies(false, false) is true
end


# (sunny == false)
# if sunny is true, then (sunny == false) is false
# if sunny is false, then (sunny == false) is true


x = if 2 > 1: "greater" else: "lower" end
check:
  x is "greater"
end

"Exercise 16"
# Define the function image-area, which counts the number of pixels in a given image. See exercise 6 for ideas.

fun image-area(img):
  image-width(img) * image-height(img)
where:
  image-area(circle(30, "solid", "red")) is 3600
  image-area(rectangle(40, 20, "solid", "yellow")) is 800
end

circle(30, "solid", "red")

"Exercise 17"
# Define the function image-classify, which consumes an image and conditionally produces "tall" if the image is taller than wide, "wide" if it is wider than tall, or "square" if its width and height are the same. See exercise 8 for ideas.

fun image-classify(img):
  if image-height(img) > image-width(img):
    "tall"
  else if image-width(img) > image-height(img):
    "wide"
  else:
    "square"
  end
where:
    image-classify(square(20, "outline", "blue")) is "square"
    image-classify(rectangle(60, 30, "outline", "red")) is "wide"
    image-classify(rectangle(30, 60, "outline", "red")) is "tall"
end

"Exercise 18"
# Define the function string-join, which consumes two strings and appends them with "_" in between. See exercise 2 for ideas.

fun string-join(str1, str2):
  part1 = string-append(str1, "_")
  ans = string-append(part1, str2)
  ans
where:
  string-join("my name is", "John Smith") is "my name is_John Smith"
  string-join("Welcome to", "Room 204") is "Welcome to_Room 204"
end

"exercise 19"
# Define the function string-insert, which consumes a string str plus a number i and inserts "_" at the ith position of str. Assume i is a number between 0 and the length of the given string (inclusive). See exercise 3 for ideas. Ponder how string-insert copes with "". 

fun string-insert(str, i):
  str1 = string-substring(str, 0, i)
  str2 = string-append(str1, "_")
  str3 = string-substring(str, i, string-length(str))
  string-append(str2, str3)
where:
  string-insert("2026-07-27Name of file", 10) is "2026-07-27_Name of file"
end

string-substring("2026-07-27Name of file", 0, 10)
string-substring("2026-07-27Name of file", 10, string-length("2026-07-27Name of file"))

"Exercise 20"
# Define the function string-delete, which consumes a string plus a number i and deletes the ith position from str. Assume i is a number between 0 (inclusive) and the length of the given string (exclusive). See exercise 4 for ideas. Can string-delete deal with empty strings?

fun string-delete(str, i):
  str1 = string-substring(str, 0, i)
  string-append(str1, string-substring(str, i + 1, string-length(str)))
where:
  string-delete("Hello_ my name is John.", 5) is "Hello my name is John."
  string-delete("I really cant help you.", 12) is "I really can help you."
end
  
string-delete("Hello_ my name is John.", 5)