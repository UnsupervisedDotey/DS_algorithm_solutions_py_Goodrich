"""

从代码段 4-12 使用重复平方的 power函数的版本中，实现一个非递归的实例。

"""


# 原函数 4-12
def power(x, n):
    """Compute the value x**n for integer n."""

    if n == 0:
        return 1

    else:

        partial = power(x, n // 2)  # rely on truncated division
        result = partial * partial

        if n % 2 == 1:  # if n odd, include extra factor of x
            result *= x

        return result


# 非递归
def power_non_recursive(x, n):
    res = 1
    for i in range(n):
        res *= x
    return res


print(power_non_recursive(2, 10))
