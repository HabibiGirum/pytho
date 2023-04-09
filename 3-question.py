# 3. write a float method rectangle() that computes and returns the area of a rectangle
#     using its two float formal parameters h and w where h is the height and w is the width of the rectangle.


def rectangle(height,width):
    area = height*width
    return area

height= int(input("enter the height of rectangle\n"))
width = int(input("enter the width of rectangle\n"))

area = rectangle(height,width)

print("The area of the rectangle is", area)
