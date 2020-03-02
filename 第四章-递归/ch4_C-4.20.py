"""
给定一个未排序的整数序列 S 和整数 k， 描述一个递归算法，用于对 S 中的元素重新排序，使得所有小于等于 k 的元素在所有大于k的元素之前。
在这个含有 n 个值的序列中，算法的时间复杂度是多少 ？
"""

from typing import List


def recursive_half_sort(_array: List[int], k: int, index: int = 0):
    """
    时间复杂度 O(n)，空间复杂度 O(1)

    :param _array:
    :param k:
    :param index:
    :return:
    """

    if index == len(_array) - 1:

        if _array[index] <= k:
            return [_array[index]], "放在前"
        else:
            return [_array[index]], "放在后"

    else:
        inner_array, signal = recursive_half_sort(_array, k, index + 1)

        if _array[index] <= k:
            return [_array[index]] + inner_array, "放在前"
        else:
            return inner_array + [_array[index]], "放在后"


print(recursive_half_sort(_array=[5, 4, 3, 2, 1], k=2))
