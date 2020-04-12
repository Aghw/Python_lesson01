#!/usr/bin/env python

def sleep_in(weekday, vacation):
    return (not weekday or vacation)


def monkey_trouble(a_smile, b_smile):
    return not (a_smile ^ b_smile)

def sum_double(a, b):
    return (a + b if a != b else 4 * a)

def diff21(n):
    return (2 * (n-21) if n > 21 else 21 - n)

def parrot_trouble(talking, hour):
    return  (talking and (hour < 7 or hour > 20))

def makes10(a, b):
    return (10 == a or 10 == b or 10 == (a + b))

def near_hundred(n):
    return (abs(n-100) <= 10 or abs(n-200) <= 10)

def pos_neg(a, b, negative):
    return (negative and (a < 0) and (b < 0) or (not negative and (a >= 0 and b < 0 or b >= 0 and a < 0)))

def not_string(str):
    return (str if str[0:3] == 'not' else 'not ' + str)

def missing_char(str, n):
    return str[:n] + str[n + 1: ]

def front_back(str):
    return (str if len(str) == 1 else str[-1:] + str[1:-1] + str[:1])

def front3(str):
    return (str + str + str if len(str) < 3 else str[0:3] + str[0:3] + str[0:3])
