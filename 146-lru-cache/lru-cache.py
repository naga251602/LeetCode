class LRUCache:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__size = 0
        self.__cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.__cache:
            self.__cache.move_to_end(key)

        return self.__cache.get(key, -1)
        
    def put(self, key: int, value: int) -> None:
        if key in self.__cache:
            self.__cache[key] = value
        elif self.__capacity == self.__size:
            item = list(self.__cache.keys())[0]
            del self.__cache[item]
            self.__cache[key] = value
        else:
            self.__cache[key] = value
            self.__size += 1
        
        self.__cache.move_to_end(key)



        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)