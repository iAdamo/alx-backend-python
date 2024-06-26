#!/usr/bin/env python3
"""Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns their sum as a float.
    """
    return float(sum(mxd_lst))


# print(sum_mixed_list.__annotations__)
# mixed = [5, 4, 3.14, 666, 0.99]
# ans = sum_mixed_list(mixed)
# print(ans == sum(mixed))
# print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans))
