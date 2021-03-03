# Missing number
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3659/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual = sum(nums)
        expected = len(nums) * (len(nums) + 1)//2
        return expected - actual