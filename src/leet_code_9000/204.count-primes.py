# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        primes = [False for i in range(n + 1)]
        for i in range(2, n):
            if primes[i] == False:
                count += 1
                j = 2
                while j * i < n:
                    primes[j * i] = True
                    j += 1
        return count


# @lc code=end
