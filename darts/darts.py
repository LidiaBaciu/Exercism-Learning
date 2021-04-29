from math import sqrt

def score(x, y):
    radius = sqrt(x*x + y*y)
    if radius <= 1.0:   return 10
    if radius <= 5.0:   return 5
    if radius <= 10.0:  return 1
    return 0