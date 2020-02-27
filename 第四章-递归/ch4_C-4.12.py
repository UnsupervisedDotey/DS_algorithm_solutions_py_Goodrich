"""
在只使用加法和减法的情况下，给出一个递归算法，来计算两个正整数m和n的乘积
"""


def recursive_multiply(m: int, n: int, n_start: int = 1):
    """递归算法 正整数 m 和 n 相乘，返回正整数结果"""
    if n_start == n:
        return m
    else:
        return recursive_multiply(m, n, n_start+1) + m


print(recursive_multiply(9, 9))
print(recursive_multiply(12, 12))
