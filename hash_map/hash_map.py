from typing import Any

class HashMap:
    def __init__(self, size: int) -> None:
        # Run `python3 hash_map.py` to execute hash map.
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash_function(self, key: str) -> int:
        """
        Calculates the hash value for the key through unicode(ord)
        param key: string
        return index: int
        """
        sum = 0 
        for i in range(len(key)):
            sum = sum + ord(key[i])
        index = sum % self.size

        return index

    def put(self, key: str, attribute: Any) -> None:
        """
        Adds the key and its attributes(values) to hash table.
        param key: string
        param attribute: any
        return index: int
        """
        index = self.hash_function(key)
        while self.keys[index] is not None:
            index += 1
        self.keys[index] = key
        self.values[index] = attribute
        return     

    def get(self, key: str) -> Any:
        """
        Gets the attributes of given key from hash table.
        param key: string
        return values : Any
        """
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index +=1
        
        return None


h = HashMap(10)
h.put("apple", 10)
h.put("banana", 15)
h.put("paple", 20)
h.put("alppe", 40)

value = h.get("apple")
value1 = h.get("banana")
value3 = h.get("paple")
value4 = h.get("alppe")
