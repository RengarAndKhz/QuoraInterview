import collections
import time
class Cache(object):
    def __init__(self):
        self.cache = collections.OrderedDict
        self.timeToKey = {}
        self.keyToTime = {}

    def scan(self, timeToKey):
        while True:
            time.sleep(1)
