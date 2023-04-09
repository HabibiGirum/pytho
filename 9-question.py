def ascending_order(nums):
    nums.sort()
    return nums

num_list = input("Enter a list of numbers separated by spaces: ")
num_list = num_list.split()
num_list = [int(num) for num in num_list]

sorted_list = ascending_order(num_list)

print("The numbers in ascending order are:", sorted_list)
# sorted_list = sorted(num_list)
