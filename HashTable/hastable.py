class HashTable:
    def __init__(self, size =7):
        self.data_map = [None] * size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        #compute the address from the key
        index = self.__hash(key)

        if self.data_map[index] == None:
          #initialize the list at the adress
          self.data_map[index] = []

        self.data_map[index].append([key,value])
      
    def get_item(self, key):
        index = self.__hash(key)

        if self.data_map[index] == None:
            return None

        for item in self.data_map[index]:
            if item[0] == key:
                return item[1]
            
        return None
    
    def keys(self):
        all_keys = []
        for item in self.data_map:
            if item is not None:
                for i in range(len(item)):
                    all_keys.append(item[i][0])
        return all_keys
    

myHashtable = HashTable()
myHashtable.set_item('bolts',500)
myHashtable.set_item('nuts',1000)
myHashtable.set_item('lumber',300)



print(myHashtable.keys())  

