#!/usr/bin/python3
"""
This module contains a method that determines if a given data set
is valid UTF-8 encoding.
"""
# HINT:
# A character in UTF8 can be from 1 to 4 bytes long, subjected to the
# following rules:
#
# For 1-byte character, the first bit is a 0, followed by its unicode code.
# For n-bytes character, the first n-bits are all one's, the n+1 bit is 0,
# followed by n-1 bytes with most significant 2 bits being 10.
# This is how the UTF-8 encoding would work:
#
#   Char. number range  |        UTF-8 octet sequence
#       (hexadecimal)    |              (binary)
#   --------------------+---------------------------------------------
#   0000 0000-0000 007F | 0xxxxxxx
#   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# Given an array of integers representing the data, return whether it is a
# valid utf-8 encoding.
#
# Note:
# The input is an array of integers.
# Only the least significant 8 bits of each integer is used to store the data.
# This means each integer represents only 1 byte of data.


def validUTF8(data):
    """
    Determine if a given data set is valid UTF-8 encoding.
    - Returns: True if data is valid UTF-8 encoding, False otherwise.
    - A character in UTF-8 can be 1 to 4 bytes long.
    - The data set can contain multiple characters.
    - The data will be represented by a list of integers, where each integer
        represents a byte, therefore you only need to handle the 8 least
        significant bits of each integer.
    """
    # number of bytes in the current UTF-8 character being processed
    number_of_bytes = 0
    mask = 255  # 11111111 in binary (8 bits)

    for byte in data:
        # Check if the first bit is a 0
        if number_of_bytes == 0:
            # mask out the first bit
            byte = byte & mask
            # Check if the first 5 bits are 110 (0b110xxxxx)
            if (byte >> 5) == 0b110:
                number_of_bytes = 1
            # Check if the first 4 bits are 1110 (0b1110xxxx)
            elif (byte >> 4) == 0b1110:
                number_of_bytes = 2
            # Check if the first 3 bits are 11110 (0b11110xxx)
            elif (byte >> 3) == 0b11110:
                number_of_bytes = 3
            # check if the first bit is a 1 (0b1xxxxxxx)
            elif (byte >> 7):
                return False
        else:
            # Check if the first 2 bits are 10 (0b10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            # Decrement the number of bytes in the current UTF-8 character
            number_of_bytes -= 1

    return number_of_bytes == 0
