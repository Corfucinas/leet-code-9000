# -*- coding: utf-8 -*-
class forrange(object):
    def __init__(self, startOrStop, stop=None, step=1):
        if step == 0:
            raise ValueError("forrange step argument must not be zero")
        if not isinstance(startOrStop, int):
            raise TypeError("forrange startOrStop argument must be an int")
        if stop is not None and not isinstance(stop, int):
            raise TypeError("forrange stop argument must be an int")

        if stop is None:
            self.start = 0
            self.stop = startOrStop
        else:
            self.start = startOrStop
            self.stop = stop

        self.step = step

    def __iter__(self):
        return self.foriterator(self.start, self.stop, self.step)

    class foriterator:
        def __init__(self, start, stop, step):
            self.currentValue = None
            self.nextValue = start
            self.stop = stop
            self.step = step

        def __iter__(self):
            return self

        def next(self):
            if self.step > 0 and self.nextValue >= self.stop:
                raise StopIteration
            if self.step < 0 and self.nextValue <= self.stop:
                raise StopIteration
            self.currentValue = forrange.forvalue(self.nextValue, self)
            self.nextValue += self.step
            return self.currentValue

    class forvalue(int):
        def __new__(cls, value, iterator):
            value = super(forrange.forvalue, cls).__new__(cls, value)
            value.iterator = iterator
            return value

        def update(self, value):
            if not isinstance(self, int):
                raise TypeError("forvalue.update value must be an int")
            if self == self.iterator.currentValue:
                self.iterator.nextValue = value + self.iterator.step
