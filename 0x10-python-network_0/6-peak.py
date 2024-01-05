#!/usr/bin/python3
def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    if len(list_of_integers) == 0:
        return None
    return sorted(list_of_integers)[-1]
