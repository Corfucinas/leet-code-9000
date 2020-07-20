# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        totalPoints = len(coordinates)
        if totalPoints < 3:
            return True

        # otherwise lets calculate area of 3 points and if zero move the window to the end of the matrix
        index = 0
        while index + 2 < len(coordinates):
            p1 = coordinates[index]
            p2 = coordinates[index + 1]
            p3 = coordinates[index + 2]

            # find area should be 0 else return false
            if not self.isAreaZero(p1, p2, p3):
                return False
            index += 1
        return True

    def isAreaZero(self, p1, p2, p3):
        area = (
            p1[0] * (p2[1] - p3[1])
            + p2[0] * (p3[1] - p1[1])
            + p3[0] * (p1[1] - p2[1])
        )
        return area == 0


# @lc code=end
