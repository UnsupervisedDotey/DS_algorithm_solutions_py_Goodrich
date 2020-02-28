"""
编写一个递归函数，该函数将输出一个含有n个元素的集合的所有子集，没有任何重复的子集
"""
from itertools import combinations
from pprint import pprint


def recursive_subset(_s: set, num: int):
    """ 将输出一个含有n个元素的集合的所有子集,
    输入 一个集合
    返回 一个列表 装着很多集合

    时间复杂度 O(n)，空间复杂度 O(n^2）？？不知道python自带的combination的复杂度是多少
    """
    if num == 2:
        return [{None}] + [{each} for each in _s]

    else:
        return recursive_subset(_s, num-1) + [set(each) for each in list(combinations(_s, num-1))]


s = {1, 2, 3, 4, 5}
pprint(recursive_subset(s, len(s)+1))
