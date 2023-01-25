'''class to model the Node
it is a simple object that wont model much '''
class Node:
    ''' an object for storing a single nore of a linked list
    models two attributes - data and link to the next node in the list'''
    data = None # instance variables
    next_node = None

    # constructor
    def __init__(self, data):
        self.data = data

    '''Adding a representation of this object using the repr function'''
    def __repr__(self) -> str:
        '''provide a string representation of what we want to be printed in the console 
        when we pring this object'''
        return "<Node data: %s>" %self.data

n1 = Node(10)
#print(n1)
n2 = Node(20)
#n1.next_node = n2
#print(n1.next_node)

''' The LinedList class is going to define the head of the list
and this attribut models the only node that the list is going to have a reference to '''
class LinkedList:
    '''Singaly Linked List'''
    # COnstructor
    def __init__(self) -> None:
        self.head = None # initially the list is empty
    def is_empt(self):
        return self.head == None
    def size(self): # linear time O(n)
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        '''adds a new node containing data at the head of the list
        this operation takes O(1) which our best scenario'''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        '''
        search for the first node contianing data the matches the key
        returns the node or None if not found

        Take O(n) or linear time 
        '''
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next_node
        return None
    def insert(self, data, index):
        '''inserts a new node containing data at index position
        insertion take constant time 
        but finding the node at insertion point take linear time 
        therefore it take an overall linear time'''
        if index == 0: # adding at the beginning
            self.add(data)
        if index > 0:
            new_node = Node(data)
            position = index
            current = self.head
            while position>1:
                current = current.next_node
                position = position - 1
            prev_node = current
            next_node = current.next_node

            # inserting the new_node between prev and next
            prev_node.next_node = new_node
            new_node.next_node = next_node


    def insert_at_tail(self,data):
        newNode = Node(data)
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = newNode



    def __repr__(self) -> str:
        '''Returns a string representation of the list
        Takes O(n) time'''
        nodes = []
        current = self.head # maintain a pointer to the head
        while current:
            if current is self.head:
               nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" %current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node # moving current/pointer forward
        return '->'.join(nodes)
    
    def remove(self,key):
        '''Doc string
        remove node containing data that matches the key, return the node removed or none if not found
        take linear time '''
        current = self.head
        prev = None
        found = False
        while current and not found: # if not current, means we reached end of the list and did not find the key
            ''' here we have 3 cases that we might run into
            1. key matches the data and data is in the head of the list.
                this is the special case because the target node does not have a previous node
            2. the node matching the data but it is not the head
            3. current doesnt not contain the data just increment the pointer
                 '''
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node # head points to the second node
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node
        return current # return the node being removed

    def remove_at_index(self, index):
        if self.head == None:
            return None
        pos = 0
        current = self.head
        prev = None
        
        while current.next_node and pos < index:
            prev = current
            current = current.next_node
            pos += 1

        if pos < index:
            return None # index out of range
        elif index == 0:
            self.head = current.next_node
        else:
            prev.next_node = current.next_node

        return current

    
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.head = prev
    
    def read_at_index(self, index):
        if self.head is None:
            return None
        current = self.head
        pos = 0
        while current.next_node and pos < index:
            current = current.next_node
            pos += 1
        if index == 0:
            return self.head
        elif pos < index:
            return None
        else: 
            return current


                        

            


       

                

l = LinkedList()
# l.head = n1
# print(l.size())
print(l.size())
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.insert(40,2)
l.insert_at_tail(50)
l.insert_at_tail(60)
print(l.size())
print(l)
#l.remove(4)
#l.remove(50)
#l.remove_at_index(0)
l.reverse()
print(l)

print(l.read_at_index(40))

#print(l.search(40))