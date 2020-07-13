# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start

from typing import List


class Solution:
    def searchInsert(  #  type: ignore
        self, nums: List[int], target: int
    ) -> int:
        for i in nums:
            if i == target or target < i:
                return nums.index(i)
            elif target not in nums:
                nums.append(target)
                return sorted(nums).index(target)


# @lc code=end
