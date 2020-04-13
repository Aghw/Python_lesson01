#!/usr/bin/env python

'''
Given a string and a non-negative int n, return a larger
string that is n copies of the original string.
'''
def string_times(str, n):
    temp = ''
    for i in range(n):
        temp += str
    return temp

'''
Given a string and a non-negative int n, we'll say that the front
of the string is the first 3 chars, or whatever is there if
the string is less than length 3. Return n copies of the front;
'''
def front_times(str, n):
    temp = str if len(str) < 3 else str[0:3]
    ret = ''
    for i in range(n):
        ret += temp
    return ret

'''
Given a string, return a new string made of every
other char starting with the first, so "Hello" yields "Hlo".
'''
def string_bits(str):
    start_str = str[:1]
    new_str = str[1:]

    if len(new_str) <= 1:
        return start_str

    for i in range(new_str): ## pick every other character
        if i % 2 != 0:
            start_str += new_str[i]
    return start_str

'''
Given a non-empty string like "Code" return a string like "CCoCodCode".
'''
def string_splosion(str):
    temp = ''
    while len(str) > 0:
        temp = str + temp
        str = str[:-1]
    return temp

'''
Given a string, return the count of the number of times that a
substring length 2 appears in the string and also as the last 2
chars of the string, so "hixxxhi" yields 1
(we won't count the end substring).
'''
def last2(str):
    counter = 0
    temp = str[-2:]
    new_str = str[:-1]
    for i in range(len(new_str)):
        if new_str[i:i+2] == temp:
            counter += 1
    return counter

'''
Given an array of ints, return the number of 9's in the array.
'''
def array_count9(nums):
    return nums.count(9)

'''
Given an array of ints, return True if one of the first 4 elements
in the array is a 9. The array length may be less than 4.
'''
def array_front9(nums):
    return nums[:4].count(9) > 0

'''
Given an array of ints, return True if the sequence of
numbers 1, 2, 3 appears in the array somewhere.
'''
def array123(nums):
    temp = [1, 2, 3]
    new_nums = nums[:-2]
    for i in range(len(new_nums)):
        if nums[i:i+3] == temp:
            return True
    return False

'''
Given 2 strings, a and b, return the number of the positions
where they contain the same length 2 substring. So "xxcaazz"
and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings
appear in the same place in both strings.
'''
def string_match(a, b):
    counter = 0
    a_sub = a[:-1]
    for i in range(len(a_sub)):
        if b[i:i+2] == a[i:i+2]:
            counter += 1
    return counter
