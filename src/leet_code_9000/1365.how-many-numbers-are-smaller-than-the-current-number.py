# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        output = []
        counter = 0
        for i in nums:
            for k in nums:
                if i > k:
                    counter += 1
            output.append(counter)
            counter = 0
        return output


# @lc code=end
