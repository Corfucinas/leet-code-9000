# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start

from math import factorial


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n

        return count


# @lc code=end
