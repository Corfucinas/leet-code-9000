# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = []
        x = 0
        for i in nums:
            x += i
            a.append(x)
        return a


# @lc code=end
