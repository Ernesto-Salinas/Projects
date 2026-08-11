use context starter2024
#|
overlay-align("left", "top",
  square(30, "solid", "bisque"), square(50, "solid", "dark-green"))
|#

s1 = square(50, "solid", "orange")
s2 = square(50, "solid", "blue")
s3 = square(50, "solid", "green")

two-squares = above(s1, s2)
above(two-squares, s3)