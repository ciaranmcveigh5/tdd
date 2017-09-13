# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. Input to the function is guaranteed to be a single string.
#
# Examples of valid inputs: 1.2.3.4 123.45.67.89
#
# Examples of invalid inputs: 1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089

import unittest

def isIpValid(ip):
    ipOctets = splitIpIntoOctets(ip)
    if isIpLengthValid(ipOctets) and isOctetValidValue(ipOctets):
        return True
    else:
        return False

def splitIpIntoOctets(ip):
    ipOctets = ip.split('.')
    return ipOctets

def isIpLengthValid(ip):
    if len(ip) == 4:
        return True
    else:
        return False

def isOctetValidValue(octets):
    for octet in octets:
        if isOctetMadeOfCharacters(octet) or int(octet) > 255 or int(octet) < 0 or ' ' in octet or isLeadingZeroInOctet(octet):
            return False

    return True

def isLeadingZeroInOctet(octet):
    octetNumbers = list(octet)
    if len(octetNumbers) > 1 and int(octetNumbers[0]) == 0:
        return True
    else:
        return False


def isOctetMadeOfCharacters(octet):
    try:
        int(octet)
        return False
    except ValueError:
        return True






class TestIpValidation(unittest.TestCase):

    def test_empty_ip(self):
        self.assertEqual(isIpValid(''), False)

    def test_valid_ip(self):
        self.assertEqual(isIpValid('1.2.3.4'), True)

    def test_octet_over_255_range(self):
        self.assertEqual(isIpValid('1.2.3.256'), False)

    def test_octet_below_0_range(self):
        self.assertEqual(isIpValid('1.2.-3.255'), False)

    def test_octet_is_string(self):
        self.assertEqual(isIpValid('1.2.i.hello'), False)

    def test_over_valid_ip_length(self):
        self.assertEqual(isIpValid('1.2.3.4.5'), False)

    def test_under_valid_ip_length(self):
        self.assertEqual(isIpValid('1.2.3'), False)

    def test_space_in_octet(self):
        self.assertEqual(isIpValid('1.2 .3.5'), False)

    def test_leading_zero_in_octet(self):
        self.assertEqual(isIpValid('1.02.3.4'), False)
