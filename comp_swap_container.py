"""
Counting container and value
"""

from __future__ import annotations
from typing import Iterable, TypeVar
from beartype import beartype

T = TypeVar("T")


@beartype
class CompSwapList(list[T]):
    """
    ....
    """

    @property
    def swaps(self) -> int:
        """
        Return an approximate number of swaps assuming one swap ~ two assignments

        :return: Estimated number of swaps (integer division)
        :rtype: int
        """
        return self._swaps

    @property
    def comps(self) -> int:
        """
        Return an approximate number of swaps assuming one swap ~ two assignments

        :return: Estimated number of swaps (integer division)
        :rtype: int
        """
        return self._comps

    def __init__(self, data: Iterable[T]):
        """
        Initialize the container, optionally with a list

        :param data: Optional initial data
        :type data: list[BasicType] or None
        """
        super().__init__(data)

        self._swaps: int
        self._comps: int
        self.reset_stats()  # иначе MyPy ругается не по делу =)

    def reset_stats(self) -> None:
        """
        Reset stats to zero
        """
        self._swaps = 0
        self._comps = 0

    def less(self, i: int, j: int) -> bool:
        """
        Сравнение, оператор <

        :param i: Индекс левого элемента
        :type data: int
        :param j: Индекс правого элемента
        :type data: int
        :return: a[i] < a[j]
        :rtype: bool
        """
        self._comps += 1
        return self[i] < self[j]  # type: ignore[operator]

    def swap(self, i: int, j: int) -> None:
        """
        Поменять местами два элемента

        :param i: Индекс левого элемента
        :type data: int
        :param j: Индекс правого элемента
        :type data: int
        """
        self._swaps += 1
        self[i], self[j] = self[j], self[i]
