#!/usr/bin/python3
"""
6-max_integer_test - Test module for testing max_integer
function in 6-max_integer module
"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class MaxIntergerTest(unittest.TestCase):

    """
    Test class contain many method represent each test case
    """

    def testEmpty(self):
        self.assertEqual(None, max_integer([]))

    def testOneElement(self):
        self.assertEqual(5, max_integer([5]))

    def testPositiveNumbers(self):
        self.assertEqual(22, max_integer([1, 9, 11, 22, 7, 6]))
        self.assertEqual(2, max_integer([1, 2]))
        self.assertEqual(3, max_integer([1, 2, 3]))

    def testNegetiveNumbers(self):
        self.assertEqual(-1, max_integer([-50, -6, -90, -1, -999999]))

    def testPositiveAndNegetiveNumbers(self):
        self.assertEqual(952, max_integer([-2, 5, 952, 452, -52, -52562, 523]))

    def testnotIntegerList(self):
        self.assertRaises(TypeError, max_integer, ["15", 1, 7, 9, -2, "Hello"])

    def testNotListArgument(self):
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 10.0)
        self.assertRaises(TypeError, max_integer, None)
        self.assertEqual("5", max_integer("12315"))

    def testDicArgument(self):
        self.assertRaises(KeyError, max_integer, {"1": 1, "2": 2})
        self.assertEqual(4, max_integer({0: 4, 1: 1, 2: 2}))

    def testNoArgument(self):
        self.assertEqual(None, max_integer())

    def testMoreThanOneArgument(self):
        self.assertRaises(TypeError, max_integer, [], ())
        self.assertRaises(TypeError, max_integer, [1, 2, 3, 4], 4, "Home", {})
