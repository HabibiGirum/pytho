# 2. write a float method triangle() that computes the area of a triangle using its two formal parameters
#     h and w, where h is the height and w is the length of the bases of the triangle.



def triangle(height,width):
    area = 0.5*height*width
    return area

height= int(input("enter the height of triangle\n"))
width = int(input("enter the width of triangle\n"))

area = triangle(height,width)

print("The area of the triangle is", area)
