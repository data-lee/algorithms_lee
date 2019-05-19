"""
Given an array S of n integers, are there three distinct elements
a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
{
  (-1, 0, 1),
  (-1, -1, 2)
}
"""


def three_sum(array):
    """
    :param array: List[int]
    :return: Set[ Tuple[int, int, int] ]
    """
    res = set()
    array.sort()
    for i in range(len(array) - 2):
        if i > 0 and array[i] == array[i - 1]:
            continue
        ll, r = i + 1, len(array) - 1
        while ll < r:
            s = array[i] + array[ll] + array[r]
            if s > 0:
                r -= 1
            elif s < 0:
                ll += 1
            else:
                # found three sum
                res.add((array[i], array[ll], array[r]))

                # remove duplicates
                while ll < r and array[ll] == array[ll + 1]:
                    ll += 1

                while ll < r and array[r] == array[r - 1]:
                    r -= 1

                ll += 1
                r -= 1
    return res
