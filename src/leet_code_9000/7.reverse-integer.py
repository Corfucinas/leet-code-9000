# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:  # sourcery skip: move-assign
        string = str(x)
        if x >= 2 ** 31 - 1 or x <= -(2 ** 31):
            return 0
        else:
            if x >= 0:
                reverse_string = string[::-1]
            else:
                temp = string[1:]
                temp2 = temp[::-1]
                reverse_string = "-" + temp2
            if int(reverse_string) >= 2 ** 31 - 1 or int(reverse_string) <= -(
                2 ** 31
            ):
                return 0
            else:
                return int(reverse_string)


# @lc code=end
