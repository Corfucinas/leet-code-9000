# -*- coding: utf-8 -*-
#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start

from threading import Semaphore
from typing import Callable


class Foo:
    def __init__(self):
        self.second_sem = Semaphore(1)
        self.third_sem = Semaphore(1)
        self.second_sem.acquire()
        self.third_sem.acquire()

    def first(self, printFirst: "Callable[[], None]") -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_sem.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        self.second_sem.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_sem.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        self.third_sem.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


# @lc code=end
