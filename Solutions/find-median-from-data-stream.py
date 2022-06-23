"""
Link: https://leetcode.com/problems/find-median-from-data-stream
"""


class MedianFinder:

    def __init__(self):
        self.numbers = []

    def addNum(self, num: int) -> None:
        self.numbers.append(num)

    def findMedian(self) -> float:
        self.numbers.sort()
        length_of_numbers = len(self.numbers)

        if length_of_numbers % 2 == 0:
            # Even
            middle = int(length_of_numbers / 2 - 1)
            return (self.numbers[middle] + self.numbers[middle + 1]) / 2
        else:
            middle = length_of_numbers // 2
            return self.numbers[middle]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()