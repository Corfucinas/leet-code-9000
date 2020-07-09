# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for element in nums[::-1]:
            if element == val:
                nums.remove(element)
        return len(nums)


# @lc code=end
