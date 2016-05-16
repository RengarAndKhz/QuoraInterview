import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.low = []
        heapq.heapify(self.low)
        self.high = []
        heapq.heapify(self.high)


    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.high, num)
        if len(self.high) - len(self.low) > 1:
            temp = heapq.heappop(self.high)
            heapq.heappush(self.low, -1 * temp)



    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.high) == len(self.low):
            return float((self.high[0] - self.low[0])/2.0)
        else:
            return float(self.high)



# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()