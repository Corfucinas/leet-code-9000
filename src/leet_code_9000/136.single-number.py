# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:  # type: ignore
        for unique in nums:
            if nums.count(unique) == 1:
                return unique


# @lc code=end
