"""
使用在代码段 4-11 中 实现的传统函数，绘制出 power(2,5) 函数计算的递归跟踪
"""


# 代码段 4-11， 用简单的递归计算幂函数
def power(x: int, n: int):
    """compute the value x**n for integer n."""

    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


print(power(2, 5))

"""
power(2, 5)                     -> return 2 * power(2, 5-1) = 32
                                   return 2 * 2 * 2 * 2 * 2 * 1 = 32
    power(2, 5-1)                   -> return 2 * 2 * 2 * 2 * 1
        power(2, 4-1)                   -> return 2 * 2 * 2 * 1
            power(2, 3-1)                   -> return 2 * 2 * 1
                power(2, 2-1)                   -> return 2 * 1
                    power(2, 1-1)     ->    n=0     -> return 1


"""