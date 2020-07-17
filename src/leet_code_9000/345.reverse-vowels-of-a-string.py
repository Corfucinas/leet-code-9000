# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1

        vowels = set('aeiouAEIOU')

        while i < j:
            # Swap
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            # Decrement by 1
            elif s[j] not in vowels:
                j -= 1
            # Increment by 1
            elif s[i] not in vowels:
                i += 1

        return ''.join(s)


# @lc code=end
