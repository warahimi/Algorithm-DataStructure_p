def merge_sort(list):
    '''Algorith steps:
    sorts a list in ascending order
    creates and returns a new sorted list,, in some implementations we might have sort in place
    Merge sort has 3 major steps:
    1- the divid step where we find the mid of the list and divid into sub list
    2- conquer step: we sort the sub list that we found in the divid step
                    recursively sort the sub list created in the previous step
    3- Combine: merge the sorted sub lists created in the previous step

    '''
    # base or stoping condition
    if len(list) <= 1:
        return list
    
    # 1 . Divide
    left_half, right_half = split(list)
    # 2. Conquer step: where we sort each sub list and return the sub list
    ''' recursive portion 
    we recursively call the merge_sort() on both divided sub lists
    it keeps further spliting the sub list untill we reach the stopping condidtion
    and  we have the single element list store 
    in left and right varaibles
    '''
    left = merge_sort(left_half) 
    right = merge_sort(right_half)

    # 3. merging backward 
    return merge(left, right) # since this algorithm returns a new list, at most it will have O(n) space complexity / linear

# 1. Divid
def split(list):
    '''divide the unsorted list at mid point into sub list
    returns two sub lists left and right'''

    # floor division 
    mid = len(list)//2
    # use the slicing notion of python to return the portions of the list'
    left = list[:mid]
    right = list[mid:]

    return left,right

def  merge(left, right):
    '''Merges two list or arrays and sorting them in the proccess and 
    retruns a new merged list'''
    l = []
    i = 0 # to keep track of the indices i for indice in the left list and j for indice in the right list
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j += 1
    # if the left and right sub arrays do not have the same length, if we have odd number of elements in our list

    while i < len(left):
        l.append(left[i])
        i+=1
    while j < len(right):
        l.append(right[j]) 
        j+=1
    return l

# test our merge_sort algorith
def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])

list = [4,1,8,55,4,0,1,-1,22,7]
sorted_list = merge_sort(list)
print(sorted_list)
print(verify_sorted(sorted_list))
print(verify_sorted(list))