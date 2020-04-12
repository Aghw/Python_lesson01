#!/usr/bin/env python


def name_error():
    print("This function produces NameError")
    print("Today is {}".format(today))







def type_error():
    print("This function produces TypeError")
    a = 3
    b = '6'
    print("The result is {}".format(a / b))




def syntax_error():
    print("This function produces SyntaxError")
  print("This statement is not valid sytax")




def attribute_error():
    a = "car"
    print("This function produces AttributeError")
    print("The value of a is {}".format(a.c))
