# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        clean = s.strip()
        for item in clean:
            if item == ' ':
                l = 0
            else:
                l += 1
        return l


# @lc code=end
