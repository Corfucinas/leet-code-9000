# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start

from collections import Counter

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

# @lc code=end
