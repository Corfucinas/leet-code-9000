# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        prefix = strs[0]
        for string in strs[1:]:
            while string[: len(prefix)] != prefix and prefix:
                prefix = prefix[: len(prefix) - 1]
            if not prefix:
                ""
        res = prefix
        return res


# @lc code=end
