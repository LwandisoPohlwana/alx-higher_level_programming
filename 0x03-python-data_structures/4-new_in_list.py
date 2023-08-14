#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ replaces an element in a copy of a list"""
    if idx < 0 or idx > (len(my_list)-1):
        return (my_list)

    lst_copy = [x for x my_list]
    lst_copy = element
    return (lst_copy)
