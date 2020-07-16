# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 1

        d = [0 for _ in range(n + 1)]
        d[0] = 1
        d[1] = 1

        for i in range(2, n + 1):
            d[i] = d[i - 2] + d[i - 1]

        return d[-1]


# @lc code=end
