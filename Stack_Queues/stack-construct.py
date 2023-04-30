class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.height = 1
        self.top = new_node
    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #push to the stack
    def push(self,value):
        new_node = Node(value)
        if self.height ==0:
            self.top = new_node
        else:
          new_node.next = self.top
          self.top =new_node
        self.height +=1

    #pop the first value
    def pop(self):
        if self.height == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -=1
        return temp

my_stack =Stack(4)
my_stack.push(6)
my_stack.push(8)
my_stack.push(10)
my_stack.push(12)
my_stack.print_stack()