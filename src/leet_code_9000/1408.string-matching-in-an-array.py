# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#

# @lc code=start

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substring = []
        for i in words:
            for k in words:
                if k in i and k != i and k not in substring:
                    substring.append(k)
        return substring


# @lc code=end
