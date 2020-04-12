#!/usr/bin/env python

def string_times(str, n):
    temp = ''
    for i in range(n):
        temp += str
    return temp

def front_times(str, n):
    temp = str if len(str) < 3 else str[0:3]
    ret = ''
    for i in range(n):
        ret += temp
    return ret


def string_bits(str):
    start_str = str[:1]
    new_str = str[1:]

    if len(new_str) <= 1:
        return start_str

    for i in range(new_str): ## pick every other character
        if i % 2 != 0:
            start_str += new_str[i]
    return start_str

def string_splosion(str):
    temp = ''
    while (len(str) > 0):
        temp = str + temp
        str = str[:-1]
    return temp


def last2(str):
    counter = 0
    temp = str[-2:]
    new_str = str[:-1]
    for i in range(len(new_str)):
        if new_str[i:i+2] == temp :
            counter += 1
    return counter

def array_count9(nums):
    return nums.count(9)

def array_front9(nums):
    return nums[:4].count(9) > 0

def array123(nums):
    temp = [1,2,3]
    new_nums = nums[:-2]
    for i in range(len(new_nums)):
        if nums[i:i+3] == temp :
            return True
    return False

def string_match(a, b):
    counter = 0
    a_sub = a[:-1]
    b_sub = b[:-1]
    for i in range(len(a_sub)):
        if b[i:i+2] == a[i:i+2] :
            counter += 1
    return counter
