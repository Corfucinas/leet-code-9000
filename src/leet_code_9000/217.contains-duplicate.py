# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums and len(nums) != 1:
            seen = {}

            for integers in nums:
                if integers in seen:
                    return True
                else:
                    seen[integers] = 1

        return False


# @lc code=end
