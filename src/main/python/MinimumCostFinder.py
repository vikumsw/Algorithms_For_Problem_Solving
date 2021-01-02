#!/usr/bin/env python

"""
Challenge #717
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

Algorithm copied from the Internet
"""


def minimize_color_cost(given_array):
    results = []
    helper(given_array, results, 0, -1, 0, "")
    return min(results)


def helper(given_array, results, curr_house, prev_color, curr_cost, curr_sequence):
    if curr_house == len(given_array):
        results.append((curr_cost, curr_sequence))
        return
    for i in range(0, len(given_array[0])):
        if i != prev_color:
            helper(given_array, results, curr_house + 1, i, given_array[curr_house][i] + curr_cost,
                   curr_sequence + str(i))


arr = [[1, 2, 3, 4], [1, 2, 1, 4], [6, 1, 1, 5], [2, 3, 5, 5]]
print(minimize_color_cost(arr))

arr2 = [[1, 7, 1, 4], [9, 1, 3, 6], [6, 2, 3, 5], [3, 5, 1, 9]]
print(minimize_color_cost(arr2))