#Construt a Linked List
class Node:
    def __init__(self,value):
        self.value = value
        self.next =None
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
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
        
    def set_value(self,index, value):
        temp =self.get(index)
        if temp:
          temp.value = value
          return True
        return False

        