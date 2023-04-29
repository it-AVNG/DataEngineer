#create a Node and LinkList Construct
#write get method

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.tail =new_node
        self.head =new_node
        self.length = 1
    
    def get(self,index):
        #check empty list
        if self.head == None:
            return None
        if index <0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
        