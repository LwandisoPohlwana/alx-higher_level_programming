#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replaces an element of a lis"""
    if idx >= 0 or idx < (len(my_list)-1):
        my_list[idx] = element
    return (my_list)
