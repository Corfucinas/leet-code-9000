# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start

from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums, len(nums)))  # type: ignore


# @lc code=end
