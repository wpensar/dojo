# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import unittest

from sudoku import solution

__all__ = [
    'TestSudoku',
]


class TestSudoku(unittest.TestCase):

    def test_fail(self):
        self.assertTrue(
            solution([
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
            ]),
        )


if __name__ == '__main__':
    unittest.main()
