# Distribute Candies
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/

from collections import Counter

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        counts = Counter(candyType)
        return min(len(counts), n // 2)