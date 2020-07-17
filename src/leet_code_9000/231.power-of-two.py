# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start

import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.log2(n) % 1 == 0


# @lc code=end
