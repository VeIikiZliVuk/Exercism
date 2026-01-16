"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one, list_two):
    #if list_one == list_two:
        #return EQUAL
    #if list_one in list_two or len(list_one) == 0:
        #return SUBLIST
    #if list_two in list_one or len(list_two) == 0:
        #return SUPERLIST
    #listi_one = []
    #for x in list_one:
        #if x in list_two:
            #listi_one.append(x)
    #if len(listi_one) == len(list_one):
        #return SUBLIST
    #listi_two = []
    #for x in list_two:
        #if x in list_one:
            #listi_two.append(x)
    #if len(listi_two) == len(list_two):
        #return SUPERLIST
    #else:
        #return UNEQUAL
    if list_one == list_two:
        return EQUAL
    if not list_one:
        return 'SUBLIST'
    if not list_two:
        return 'SUPERLIST'
    
    len_one = len(list_one)
    len_two = len(list_two)
    
    if len_one <= len_two:
        for i in range(len_two - len_one + 1):
            if list_two[i:i + len_one] == list_one:
                return 'SUBLIST'
    
    if len_two <= len_one:
        for i in range(len_one - len_two + 1):
            if list_one[i:i + len_two] == list_two:
                return 'SUPERLIST'
    
    return 'UNEQUAL'
        
    #str_one = ','.join(map(str, list_one))
    #str_two = ','.join(map(str, list_two))
    #if not list_one:
        #return SUBLIST
    #if not list_two:
        #return SUPERLIST
    #if str_one in str_two:
        #return SUBLIST
    #if str_two in str_one:
        #return SUPERLIST
    #return UNEQUAL