#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ prints a dictionary by ordered keys."""
    SortList = list(a_dictionary.keys())
    Sortlist.sort()
    for i in SortList:
        print("{}: {}".format(i, a_dictionary.get(i)))
