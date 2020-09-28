import math
from point import *    #homework4
p1=point(3, [1., 2., 3.])
print(p1)
p2=point(3, [6., 7., 8.])
print(p2)

print("distance p1 to p2=", p1.dist(p2))
print("Mirror values of p2=",p2.mirror())
