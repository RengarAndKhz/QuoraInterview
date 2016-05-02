from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dictionary = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dictionary:
            temp = self.dictionary.pop(key)
            self.dictionary[key] = temp
            return temp
        else: return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dictionary:
            self.dictionary.pop(key)
            self.dictionary[key] = value
        else:
            if len(self.dictionary) >= self.capacity:
                self.dictionary.popitem(last=False)
                self.dictionary[key] = value
            else:
                self.dictionary[key] = value