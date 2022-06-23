import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.dictionary = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1
        value = self.dictionary.pop(key)
        self.dictionary[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary.pop(key)
        else:
            if len(self.dictionary) >= self.max_size:
                self.dictionary.popitem(last=False)
        self.dictionary[key]=value