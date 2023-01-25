from linked_list import LinkedList

# def merge_sort(linked_list):
#     '''sort a LL in ascending order
#     1. first recursively divid the ll inot sublist containing a single node
#     2. repeadedly merge the sublist to produce the sorted sublists untill one remains
#     3. returns a soreted linked list'''

#     # stoping condition 
#     if linked_list.size() == 1:
#         return linked_list
#     elif linked_list.head is None: # if ll is empty
#         return linked_list
#     # spliting the ll into right and left half 
#     left_half, right_half = split(linked_list)
#     left = merge_sort(left_half)
#     right = merge_sort(right_half)

#     return merge(left, right)

# # Divide step or implementation of the split function 
# def split(linked_list):
#     '''Divides the unsorted ll at midpoint into sublists'''
#     if linked_list == None or linked_list.head == None:
#         left_half = linked_list
#         right_half = None
#         return left_half,right_half
#     else:
#         size = linked_list.size()
#         mid = size //2 
#         mid_node = linked_list.get_node_at_index(mid-1)
#         # slpliting the ll at mid node
#         left_half = linked_list
#         right_half = LinkedList() # new instance of ll
#         right_half.head = mid_node.next_node
#         mid_node.next_node = None

#         return left_half, right_half

# def merge(left, right):
#     ''' this function merges two linked lists, sorting by data in nodes
#     returs a new, merged list '''

#     # create a new linked list that contain nodes from merging left and right
#     merged = LinkedList()

#     # Add a fake head that is discarded later 
#     merged.add(0)

#     # set current to the head of linked list
#     current = merged.head

#     # Obtain head nodes for left and right linked list 
#     left_head = left.head
#     right_head = right.head

#     # iterate over left and right untill we reached the tail node of either 

#     while left_head or right_head:
#         # if the head node oflef is None, we are past the tail
#         # add the nod from right to merged linked list 
#         if left_head is None:
#             current.next_node = right_head
#             # call nex on right to set loop condition to false
#             right_head = right_head.next_node
#             # if the head node of right is None, we are past the tail 
#             #  add the tail node from left to merged linked list
#         elif right_head is None:
#             current.next_node = left_head
#             # call nex on left to set loop condition to False 
#             left_head = left_head.next_node
#         else:
#             # not at either tail node
#             # obtain node data to perform comparision operation 
#             left_data = left_head.data
#             right_data = right_head.data
#             # if data on left is less than right, set current to the left node
#             if left_data < right_data:
#                 current.next_node = left_head
#                 # move left head to next node
#                 left_head = left_head.next_node
#             # if data on left is greater than right 
#             # set current to the right node
#             else:
#                 current.next_node = right_head
#                 # move right head to  next node
#                 right_head = right_head.next_node
#             # move current to the next node 
#             current = current.next_node
#     return merged
def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list

    Takes O(n log n) time
    Takes O(n) space
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Takes O(log n) time
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.get_node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    Takes O(n) space
    Runs in O(n) time
    """

    # Create a new linked list that contains nodes from merging left and right
    merged = LinkedList()
    # Add a fake head that is discarded later.
    merged.add(0)
    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right as long until the tail node of both
    # left and right
    while left_head or right_head:
        # If the head node of left is None, we're at the tail
        # Add the tail node from right to the merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node 
        # If the head node of right is None, we're at the tail
        # Add the tail node from left to the merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            # If data on left is lesser than right set current to left node
            # Move left head to next node
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # If data on left is greater than right set current to right node
            # Move right head to next node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged
l = LinkedList()
l.add(44)
l.add(3);l.add(5);l.add(30);l.add(13);l.add(113);l.add(31)
l.add(-1)
print(l)
l2 = merge_sort(l)
print(l2)





