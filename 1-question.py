# # 1. write an int method cube() that returns the cube of the value inserted?


# define function cube() method
def cube(num):
    return num**3

# input from user
num = input("enter the number\n")
# convert from str type to int
num = int(num)
result = cube(num)
print("the cube of "+str(num)+" is "+str(result))
