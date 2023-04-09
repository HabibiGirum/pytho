

def Line(m,b,x):
    y=m*x+b
    return y

slope=int(input("please give me the slope of line\n"))
y_intercept = int(input("please give me the y-intercept\n"))
x_coordinate = int(input("please give me x-coordinate\n"))

y =Line(slope,y_intercept,x_coordinate)

print("the y-coordinate is ", y)