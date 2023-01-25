def binary_search(list,target):
    first = 0
    last = len(list)-1

    while first <= last:
        midpoint = (first + last) // 2 # floor division operator, rounds down to the nearest whole number
        if list[midpoint] == target: # our best case scenario
            return midpoint
        elif list[midpoint] <target:
            first = midpoint + 1 # discarding the first half of the list
        else:
            last = midpoint - 1
    return None
def varify(index):
    if index is not None:
        print("Index found at index: ", index)
    else:
        print("Target not found in the list")
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers2 = [i for i in range(1,21)]
result = binary_search(numbers,9)
varify(result)
result = binary_search(numbers2,12)
varify(result)

# this was an iterative solution of bineary search where we used a loop type 