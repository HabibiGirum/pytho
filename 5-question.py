
def intersect(m1,b1,m2,b2):

    if m1==m2:
        return 0 # the lines are parallel, no intersection.
        
    else:
        return 1 # the lines intersect.


m1=int(input("please give me m1\n"))
b1=int(input("please give me b1\n"))
m2=int(input("please give me m2\n"))
b2=int(input("please give me b2\n"))

result = intersect(m1,b1,m2,b2)
print("the lines intersect:", result)


