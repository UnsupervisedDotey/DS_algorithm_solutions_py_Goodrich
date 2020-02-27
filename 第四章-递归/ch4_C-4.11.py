"""
描述一个有效的递归函数来求解元素的唯一性问题，在不使用排序的最坏情况下运行时间最多是 O(n^2)
"""
from typing import List


def if_equal(_list: List[int], index: int, sub_index: int):
    if _list[index] == _list[sub_index]:
        return False
    else:
        return True


def good_recursive_unique(_list: List[int], index: int, sub_index: int = 0):
    """检查一个列表里是否有重复出现的元素，返回是或否"""
    # print(index, sub_index)

    if index == len(_list)-1:
        return True

    else:
        res = True
        for sub_index in range(index+1, len(_list)):
            res = res * if_equal(_list, index, sub_index)

            # print(index, sub_index, res)

        return res * good_recursive_unique(_list, index+1)


def translate():
    # target_list = [1, 2, 3, 4, 0]
    target_list = [1, 2, 2, 3, 1]
    res = good_recursive_unique(target_list, 0)

    if res == 1:
        return True, "all numbers in the list is different"
    else:
        return False, "there are same numbers in this list"


print(translate())
