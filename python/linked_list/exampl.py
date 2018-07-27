import re
import sys
class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleList(object):

    head = None
    tail = None
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def show(self):
        print "Show list data:"
        current_node = self.head
	prev_data = 'None'
        present_data = ''
        next_data = ''
	da = 0
        while current_node is not None:
	    if hasattr(current_node.prev,"data"):
		prev_data = current_node.prev.data
            present_data = current_node.data
            if hasattr(current_node.next, "data"):
		next_data = current_node.next.data
	    else:
		next_data = 'None'
	    if (present_data == 'B'):
		da+=1
	    if (prev_data == 'L')&(next_data == 'L')&(present_data == 'B'):
		da-=1
	    elif(prev_data == 'L')&(next_data == 'None')&(present_data == 'B'):
		da-=1
	    elif(prev_data == 'None')&(next_data == 'L')&(present_data == 'B'):
		da-=1
	    current_node = current_node.next
	print da

d = DoubleList()
arg1=sys.argv
numm = str(arg1)
print numm
for i in numm:
    d.append(i)
d.show()
