#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list."""
    NewList = list(map(lambda x: replace if x == search else x, my_list))
    return (NewList)
