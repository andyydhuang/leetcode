class LRUCache:
    dic = collections.defaultdict()
    max_size = None
    stack = []

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.dic.clear()
        self.stack.clear()        

    def get(self, key: int) -> int:
        if key in self.dic:
            #Recently used 
            self.stack.remove(key)
            self.stack.append(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.stack.remove(key)
            self.stack.append(key)
            self.dic[key] = value        
        else:        
            if len(self.dic.keys()) == self.max_size:
                #Remove least used
                self.dic.pop(self.stack[0])
                self.stack.pop(0)

            #Put new into LRU cache  
            self.stack.append(key)    
            self.dic[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)