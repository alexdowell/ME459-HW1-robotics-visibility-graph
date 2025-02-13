import math as m #library is needed for square root operation

def magnitude(x_1, y_1, x_2, y_2):    # function for determining distance between two points
    magnitude = m.sqrt((x_2 - x_1)**2+(y_2 - y_1)**2)
    
    return magnitude
    
x_1 = 2  #starting point
y_1 = 1

x_2 = 3  #ending point
y_2 = 2
distance = magnitude(x_1, y_1, x_2, y_2)

print("the distance from the point (", x_1, ",",y_1 ,") to point (", x_2, ",",y_2 ,") is" ,distance)