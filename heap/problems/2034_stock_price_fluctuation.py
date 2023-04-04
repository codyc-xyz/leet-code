# You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

# Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

# Design an algorithm that:

# Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
# Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
# Finds the maximum price the stock has been based on the current records.
# Finds the minimum price the stock has been based on the current records.
# Implement the StockPrice class:

# StockPrice() Initializes the object with no price records.
# void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
# int current() Returns the latest price of the stock.
# int maximum() Returns the maximum price of the stock.
# int minimum() Returns the minimum price of the stock.


class StockPrice:

    def __init__(self):
        self.hm = {}
        self.minHeap = []
        self.maxHeap = []
        self.latest = [-1, 0]
        
    def update(self, timestamp: int, price: int) -> None:
        self.hm[timestamp] = price

        heapq.heappush(self.minHeap, [price, timestamp])
        heapq.heappush(self.maxHeap, [-price, timestamp])
        if timestamp >= self.latest[0]:
            self.latest = [timestamp, price]
        
    def current(self) -> int:
        return self.latest[1]
        
    def maximum(self) -> int:
        price, time = self.maxHeap[0]
        while self.hm[time] != -price:
            heapq.heappop(self.maxHeap)
            price, time = self.maxHeap[0]

        return -price
        
    def minimum(self) -> int:
        price, time = self.minHeap[0]
        while self.hm[time] != price:
            heapq.heappop(self.minHeap)
            price, time = self.minHeap[0]
        return price



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()