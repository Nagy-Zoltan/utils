from bisect import bisect_left
from math import isclose


def get_closest_in_sorted_list(L: list[float], num: float):
    closest_candidates = {}
    bisect_index = bisect_left(L, num)
    for i in range(-1, 2):
        try:
            index = bisect_index + i
            if index < 0:
                continue
            closest_candidates[index] = L[index]
        except IndexError:
            pass

    return min(closest_candidates, key=lambda key: abs(closest_candidates[key] - num))
