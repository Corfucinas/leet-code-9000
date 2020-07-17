# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=1374 lang=python3
#
# [1374] Generate a String With Characters That Have Odd Counts
#

# @lc code=start


class Solution:
    def generateTheString(self, n: int) -> str:
        return ''.join('a' * ((n - 1) // 2 * 2 + 1) + 'b' * (1 - n % 2))


# @lc code=end
