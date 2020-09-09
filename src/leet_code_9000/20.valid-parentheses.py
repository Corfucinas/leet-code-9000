# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "[": "]", "{": "}"}
        valid = []
        for item in s:
            if item in brackets:
                valid.append(brackets[item])
            else:
                if not (valid and valid.pop() == item):
                    return False
        return not valid


# @lc code=end
