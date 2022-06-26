"""
Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        len_cardPoints = len(cardPoints)
        if k == len_cardPoints:
            return sum(cardPoints)
        if k == 1:
            return max(cardPoints[0],cardPoints[-1])
        max_sum = sum(cardPoints[0:k])
        current_sum = max_sum
        for i in range(k):
            current_sum -= cardPoints[k-i-1]
            current_sum += cardPoints[len_cardPoints-i-1]
            max_sum = max(max_sum,current_sum)
        return max_sum