"""

假设给出一个含有 n 个元素的序列 S，这个序列是包含不同元素的"升序序列"。给定一个数 k，描述一个递归算法找到 S 中总和为 k 的两个整数（如果
这样的一对整数存在）。算法的时间复杂度是多少？

"""

from typing import List


def recursive_find_pair(_array: List[int], k: int, outer_index: int = 0):
    """

    :param _array:
    :param k: 这个序列是包含不同元素的"升序序列"
    :param outer_index
    :return:
    """

    if outer_index == len(_array):
        return []

    for inner_index in range(outer_index + 1, len(_array)):

        print(outer_index, inner_index)

        p1 = _array[outer_index]
        p2 = _array[inner_index]

        if p1 + p2 == k:
            return [p1, p2]

        if inner_index == len(_array)-1:
            return recursive_find_pair(_array, k, outer_index+1)


print(recursive_find_pair(_array=[1, 2, 3, 4, 5, 6, 7], k=6))
