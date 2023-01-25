def recursive_binary_search(list, target): # retrun true or false
    if len(list) == 0: # if list is empty
        return False
    else:
        midpoint = (len(list)) //2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

numbers = [1,2,3,4,5,6,7]

print(recursive_binary_search(numbers,5))
print(recursive_binary_search(numbers,50))

# we reached at a logarithmatic run time in this case because we keep calling the function 
# with a samaller list 