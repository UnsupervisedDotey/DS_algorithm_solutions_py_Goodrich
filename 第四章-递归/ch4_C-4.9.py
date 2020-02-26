"""
写一个简短的递归Python函数，用于在不使用任何循环的条件下查找一个序列中的最小值和最大值
原创
"""
from typing import List


def recursive_min_max(target: List[int], index: int, _min: float, _max: int):
    """迭代训练，返回列表的最小值和最大值 时间复杂度 O(n) 空间复杂度 O(n)  线性递归"""
    # 基本情况 到列表的最后一个位置时
    if index == len(target) - 1:

        if target[index] > _max:
            _max = target[index]

        if target[index] < _min:
            _min = target[index]

        return _min, _max

    else:
        _min, _max = recursive_min_max(target, index+1, _min, _max)

        if target[index] > _max:
            _max = target[index]

        if target[index] < _min:
            _min = target[index]

        return _min, _max


print(recursive_min_max([1, 2, 3, 4, 5, 3, 111, 0, -133], 0, float("inf"), 0))
