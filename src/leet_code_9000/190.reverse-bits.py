# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n >>= 1
            power -= 1
        return ret


# @lc code=end
