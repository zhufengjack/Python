import math

print math.sqrt(9)

def area_triangle_sss(side1,side2,side3):
  """
  Returns area of a triangle, given the lengths of its three sides.

  """
  semi_perim=(side1+side2+side3)/2.0
  return math.sqrt(semi_perim*
                  (semi_perim - side1)*
                  (semi_perim - side2)*
                  (semi_perim - side3)
                  )

print area_triangle_sss(4,4,4)
