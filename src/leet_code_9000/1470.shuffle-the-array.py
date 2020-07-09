# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[0:n], nums[n:]):
            res += [i, j]
        return res


# @lc code=end
