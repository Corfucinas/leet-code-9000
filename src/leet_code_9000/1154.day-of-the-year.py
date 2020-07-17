# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
#

# @lc code=start

import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        year_check = int(date[0:4])
        leap = 0
        if year_check % 400 == 0:
            leap = 1
        if year_check % 4 == 0 and year_check % 100 != 0:
            leap = 1
        day1 = datetime.datetime(
            int(date[0:4]), int(date[5:7]), int(date[8:10])
        )
        day2 = datetime.datetime(int(date[0:4]), int(12), int(31))
        return 365 - (day2 - day1).days + leap


# @lc code=end
