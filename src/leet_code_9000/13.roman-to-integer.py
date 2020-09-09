# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        integer = 0
        for i in range(len(s)):
            if i > 0 and rom[s[i]] > rom[s[i - 1]]:
                integer += rom[s[i]] - 2 * rom[s[i - 1]]
            else:
                integer += rom[s[i]]
        return integer


# @lc code=end
