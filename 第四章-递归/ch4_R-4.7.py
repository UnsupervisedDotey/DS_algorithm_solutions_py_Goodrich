"""
描述一个递归函数，它可以把一串数字转换成对应的整数。 例如 13531‘ 对应的整数位13531
"""


def recursive_str_to_int(string: str, index: int):
    """把string变成对应的整数
    时间空间复杂度都是 O（n）
    """

    if index == len(string)-1:
        return int(string[-1]) * 1
    else:
        return recursive_str_to_int(string, index+1) + int(string[index]) * 10 ** (len(string)-1-index)


print(isinstance(recursive_str_to_int(string='1359301', index=0), int))
