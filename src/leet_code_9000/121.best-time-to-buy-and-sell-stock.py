# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit, stock = float("-inf"), prices[0]
        for p in prices:
            profit = max(profit, p - stock)
            stock = min(stock, p)
        return int(profit)


# @lc code=end
