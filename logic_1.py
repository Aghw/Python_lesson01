#!/usr/bin/env python

def cigar_party(cigars, is_weekend):
    return (40 <= cigars <= 60 if not is_weekend else 40 <= cigars)

def date_fashion(you, date):
    return (0 if you <= 2 or date <= 2 else (2 if you >= 8 or date >= 8  else 1))

def squirrel_play(temp, is_summer):
    return (60 <= temp <= 100 if is_summer else 60 <= temp <= 90)

def caught_speeding(speed, is_birthday):
    return (0 if is_birthday and speed <= 65 else (1 if is_birthday and 66 <= speed <= 85 else (0 if speed <= 60 else (1 if 61 <= speed <= 80 else 2))))

def sorta_sum(a, b):
    return (20 if 10 <= a + b <= 19 else a + b)

def alarm_clock(day, vacation):
    return ("7:00" if not vacation and day not in [0, 6] else ("10:00" if not vacation  else ("10:00" if vacation and day not in [0, 6] else "off")))

def love6(a, b):
    return (a == 6 or b == 6 or abs(a - b) == 6 or abs(b - a) == 6 or (a + b) == 6)

def in1to10(n, outside_mode):
    return (n <= 1 or n >= 10 if outside_mode else 1 <= n <= 10)

def near_ten(num):
  return num % 10 <= 2 or abs((num % 10) - 10) <= 2
