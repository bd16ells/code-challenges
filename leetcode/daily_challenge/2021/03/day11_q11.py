from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 or amount < min(coins):
            return 0
        return self.recursive_change(sorted(coins, reverse=True), amount, [])
    
    def recursive_change(self, coins, amount, nums):
        if len(coins) == 0:
            return -1
        if sum(nums) == amount:
            return len(nums)
        
        if sum(nums) > amount:
            nums = nums[:-1]
        
        if sum(nums) + coins[0] <= amount:
            nums.append(coins[0])
            return self.recursive_change(coins, amount, nums)

        
        
        return self.recursive_change(coins[1:], amount, nums)