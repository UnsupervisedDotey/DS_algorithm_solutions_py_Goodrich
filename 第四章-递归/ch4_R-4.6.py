"""
描述一个递归函数，用于计算第n个调和数（harmonic number），其中 H_n = sum(i from 1 to n) 1/i
"""


def recursive_harmonic(n: int):
    """计算第n个调和数

    时间复杂度： O（n） 因为要重复处理n次
    空间复杂度： O（n） 因为每次都要存1/n这个值
    """

    if n == 1:
        return 1
    else:
        H_n = 1/n
        return recursive_harmonic(n-1) + H_n


print(recursive_harmonic(10))
print(recursive_harmonic(2))
print(recursive_harmonic(4))


