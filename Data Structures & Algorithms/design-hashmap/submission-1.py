class MyHashMap:
    # Both time and space is O(1) - constant for accessing, deletion, and checking the existance of the key
    # Time Complexity:
    # add()       -> O(1)
    # remove()    -> O(1)
    # contains()  -> O(1)

    # Space Complexity:
    # O(1) because the array has a fixed size of 1,000,001
    # based on the constraint 0 <= key <= 1,000,000
    designed_map = [] 

    def __init__(self):
        self.designed_map = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        # adding key-value
        self.designed_map[key] = value
        

    def get(self, key: int) -> int:
        if self.designed_map[key] != None:
            return self.designed_map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.designed_map[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)