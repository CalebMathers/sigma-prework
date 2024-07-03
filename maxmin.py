# get a list of nums from the user
def get_nums():
    nums = []
    num_strings = input("Provide a list on integers, seperated by ',': ")
    num_strings = num_strings.split(",")
    # convert each num string to an int and add to list
    for num in num_strings:
        nums.append(int(num))
    return nums

# find the highest num in a list of ints
def find_highest(nums):
    highest = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > highest:
            highest = nums[i]
        i += 1
    return highest

# find the lowest num in a list of ints
def find_lowest(nums):
    lowest = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < lowest:
            lowest = nums[i]
        i += 1
    return lowest

# get the highest and lowest and return them as a list
def maxmin():
    num_list = get_nums()
    highest = find_highest(num_list)
    lowest = find_lowest(num_list)
    output = [lowest, highest]
    print(output)
    return output

maxmin()