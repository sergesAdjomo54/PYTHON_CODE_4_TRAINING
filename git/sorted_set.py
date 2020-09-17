from bisect import bisect_left
from collections.abc import Sequence
from itertools import chain


class SortedSet(Sequence):

    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items == other._items

    def __ne__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items != other._items

    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and (self._items [index] == item):
            return index
        raise ValueError("{} not found".format(repr(item)))

    def count(self, item):
        return int(item in self)

    def __add__(self, other):
        return SortedSet(chain(self._items, other._items))

    def __mul__(self, other):
        return self if other > 0 else SortedSet()

    def __rmul__(self, other):
        return self * other

