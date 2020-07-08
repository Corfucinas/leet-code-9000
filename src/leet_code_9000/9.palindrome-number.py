# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_1 = str(abs(x))
        str_2 = str_1[::-1]
        return str_1 == str_2


# @lc code=end
