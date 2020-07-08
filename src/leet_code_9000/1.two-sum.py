# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: Dict[int, int] = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []


# @lc code=end
