# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.
#
# I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.
#
# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?
#
# Example:
#
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"
#
# When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9) it comes before as a string.
#
# All numbers in the list are positive numbers and the list can be empty.
#
# Notes
#
# Don't modify the input
# For C: The result is freed.

import unittest

def orderWeight(weights):
    weightsArray = weights.split()
    positonValueArray = getPositionAndSumOfDigitsOfWeight(weightsArray)
    sortedWeights = sortValuesBasedOnSumOfDigits(positonValueArray, weightsArray)
    result = convertWeightArrayToString(sortedWeights)

    return result

def convertWeightArrayToString(weightsArray):
    return " ".join(weightsArray)

def getPositionAndSumOfDigitsOfWeight(weightsArray):
    values = []
    for i in range(0, len(weightsArray)):
        total = 0
        weightIndividualDigitsArray = list(weightsArray[i])
        for index in range(0, len(weightIndividualDigitsArray)):
            total += int(weightIndividualDigitsArray[index])
        values.append((i, total, int(weightsArray[i])))
    print(values)
    return values

def sortValuesBasedOnSumOfDigits(values, weightsArray):
    sortedWeights = []
    newValues = sorted(values, key=lambda tup: (tup[1], tup[2]))
    for i in range(0, len(newValues)):
        PositionInOriginalArray = newValues[i][0]
        sortedWeights.append(weightsArray[PositionInOriginalArray])
    return sortedWeights

class TestWeightForWeight(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(orderWeight(""), "")

    def test_get_position_and_sum_digits(self):
        self.assertEqual(getPositionAndSumOfDigitsOfWeight(["99", "100"]), [(0, 18, 99), (1, 1, 100)])

    def test_two_values(self):
        self.assertEqual(orderWeight("99 100"), "100 99")

    def test_weights_that_sum_to_same_value(self):
        self.assertEqual(orderWeight("97 90601 79 691 88"), "79 88 97 691 90601")
