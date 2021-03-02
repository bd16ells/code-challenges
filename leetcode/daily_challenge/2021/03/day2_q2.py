# Set mismatch
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/

from collections import Counter
import math

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        dupe = counts.most_common(1)[0][0]
        actual_sum = sum(nums) - dupe
        n = len(nums)
        expected_sum = n*(n+1)/2 
        return [dupe, abs(int(actual_sum-expected_sum))]