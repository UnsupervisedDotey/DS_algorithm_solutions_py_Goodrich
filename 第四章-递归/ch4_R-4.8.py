"""
Isabel 用一种有趣的方法来计算一个含有 n 个整数的序列 A 中的所有元素之和，其中 n 是 2 的幂。（长度总为复数的序列？）
她创建一个新的序列B，其大小是序列A的一半，并且设置 B[i] = A[2i] + A[2i+1] (i=0, 1, ..., (n/2) -1)。

如果B的大小为1，那么输出 B[0]; 否则用 B 取代 A，并且重复这个过程。

请问，她的这个算法的时间复杂度是多少？
"""

from typing import List
import math


def isabel(a: List[int]):
    # python中%：求模运算，相当于mod，也就是计算除法的余数，比如5%2就得到1
    # ❤ 判断一个数 是否是整数 用 它 %1 后的余数是否为0来判断

    # log函数中，底数是第二个参数噢
    # math.log(x[, base])
    assert math.log(len(a), 2) % 1 == 0, 'Your array must be a length that is a power of 2'

    if len(a) == 1:
        return a[0]
    else:
        b = [0] * (len(a) // 2)
        for i in range(len(b)):
            b[i] = a[2 * i] + a[2 * i + 1]
        return isabel(b)


print(isabel([0, 1, 2, 3, 4, 5, 6, 7]))

"""
a                               b
[0, 1, 2, 3, 4, 5, 6, 7]        [1, 5, 9, 13]
[1, 5, 9, 13]                   [6, 22]
[6, 22]                         [28]


这个递归会被执行 log(n) 次, since the array is divided in half each time
每次回需要内部循环 n/i次，总共需要n* Sum(1/2**i)，比2n小，所以是O（n）时间复杂度


Each call will require you to access all of the remaining elements, which means it will be
n + n/2 + n/4 + ...
This is equal to n* Sum(1/2**i), which is <2n
Therefore, the running time is O(n), although a much slower implementation than just adding them up element by element

"""
