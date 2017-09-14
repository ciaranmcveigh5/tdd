# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#
# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

import unittest

def moveZeros(array):
    zeroPostions = findPositionsOfZerosInArray(array)
    zeros = [0] * len(zeroPostions)
    array.extend(zeros)
    array = removeOldZerosInArray(zeroPostions, array)

    return array

def findPositionsOfZerosInArray(array):
    zeroPostions = []
    for i in range(0, len(array)):
        if array[i] == 0 and array[i] is not False:
            zeroPostions.append(i)
    return zeroPostions

def removeOldZerosInArray(zeroPositions, array):
    for i in range(0, len(zeroPositions)):
        del array[zeroPositions[i]]
        zeroPositions[:] = [position - 1 for position in zeroPositions]
    return array

class TestMovingZerosToTheEnd(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(moveZeros([]), [])

    def test_one_zero_in_array(self):
        self.assertEqual(moveZeros([0, 1]), [1, 0])

    def test_single_zero_position(self):
        self.assertEqual(findPositionsOfZerosInArray([0, 1]), [0])

    def test_multiple_zeros_position(self):
        self.assertEqual(findPositionsOfZerosInArray([0, 1, 0, 4, 5, 0]), [0, 2, 5])

    def test_multiple_zeros_in_array(self):
        self.assertEqual(moveZeros([0, 1, 0, 5, 6, 7, 7, 0]), [1, 5, 6, 7, 7, 0, 0, 0])

    def test_floats_in_array(self):
        self.assertEqual(moveZeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]), [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])

    def test_false_in_array(self):
        self.assertEqual(moveZeros([0, 1, 0, 5, False, 6, 7, 7, 0]), [1, 5, False, 6, 7, 7, 0, 0, 0])

    def test_none_in_array(self):
        self.assertEqual(moveZeros([0, 1, 0, 5, None, 6, 7, 7, 0]), [1, 5, None, 6, 7, 7, 0, 0, 0])

    def test_true_in_array(self):
        self.assertEqual(moveZeros([0, 1, 0, 5, True, 6, 7, 7, 0]), [1, 5, True, 6, 7, 7, 0, 0, 0])

    def test_string_in_array(self):
        self.assertEqual(moveZeros([0, 1, 0, 5, "hello", 6, 7, 7, 0]), [1, 5, "hello", 6, 7, 7, 0, 0, 0])