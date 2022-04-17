from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ docstring for 1. twoSum """
        store = dict()
        for i in range(len(nums)):
            sec = target - nums[i]
            if sec not in store:
                store[nums[i]] = i
            else:
                return [store[sec], i]
