# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for i in digits:
            num += str(i)
        num = int(num)  # type: ignore
        num += 1  # type: ignore
        num = str(num)
        return [int(i) for i in num]


# @lc code=end
