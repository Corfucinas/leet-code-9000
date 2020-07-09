# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(set(nums), key=nums.count)

# @lc code=end
