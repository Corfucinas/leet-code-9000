# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        memo = [0] * (len(nums) + 1)
        memo[1] = nums[0]
        for idx in range(1, len(nums)):
            _val = nums[idx]
            memo[idx + 1] = max(memo[idx], memo[idx - 1] + _val)
        return memo[-1]


# @lc code=end
