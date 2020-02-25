"""
如代码段 4-12 实现的函数所示， 使用重复平方算法， 绘制出 power(2, 18) 函数计算的递归跟踪
"""


# R-4.2 是最简单的求幂递归 时间复杂度为 O(n)，本题使用了 重复平方 计算幂函数，复杂度为 O(logN)
def power(x, n):
    """compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


print(power(2, 18))

"""

power(2, 18)                -> return 512 * 512 = 262144
    power(2, 9)                 -> return 2 * 16 * 16 = 512
        power(2, 4)                 -> return 4 * 4 = 16
            power(2, 2)                 -> return 2 * 2 = 4
                power(2, 1)                 -> return 2 * 1 * 1 = 2
                    power(2, 0)     -> n=0          -> return 1

"""