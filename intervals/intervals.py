"""
  File: intervals.py
  Description: tuples_list is an unsorted list of tuples denoting 
  intervals and a list of merged tuples sorted by the lower number of the interval

  Student Name: Arham Lodha
  Student UT EID: arl3759

  Partner Name: Tho Lam
  Partner UT EID: tml2532

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 08/24/2023
  Date Last Modified: 08/24/2023
"""

import sys


def sort_tuples(tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    lower number in the interval
    """

    return sorted(tuples_list, key=lambda x: x[0])


def merge_tuples(tuples_list):
    """
    Merge the tuples

    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
    """

    tuples_list = sort_tuples(tuples_list)

    merged = []

    for current in tuples_list:
        if len(merged) != 0:
            last_interval = list(merged[-1])

            if current[0] <= last_interval[1]:
                last_interval[1] = max(current[1], last_interval[1])
                merged[-1] = tuple(last_interval)
            else:
                merged.append(current)
        else:
            merged.append(current)
    return merged


def sort_by_interval_size(tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """

    # Add Your Code HERE ... AND REMOVE THIS Line

    return sorted(tuples_list, key=lambda x: x[1] - x[0])  # Replace this.


def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merged)

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)


if __name__ == "__main__":
    main()
