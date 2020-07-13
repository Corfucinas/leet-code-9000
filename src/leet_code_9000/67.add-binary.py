# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = val = 0
        if len(a) < len(b):
            a, b = b, a
        lengthA = len(a)
        lengthB = len(b)
        for i in range(lengthA):
            val = carry
            val += int(a[-(i + 1)])
            if i < lengthB:
                val += int(b[-(i + 1)])
            carry, val = val // 2, val % 2
            result.append(str(val))
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])


# @lc code=end
