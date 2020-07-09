# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index_to_update = 0
        for element in nums:
            if element > nums[index_to_update]:
                index_to_update += 1
                nums[index_to_update] = element

        return index_to_update + 1

# @lc code=end
