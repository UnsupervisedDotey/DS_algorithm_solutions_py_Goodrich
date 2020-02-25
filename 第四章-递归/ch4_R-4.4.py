"""
绘制函数 reverse(S, 0, 5)（代码段4-10）执行的递归追踪，其中 S = [4, 3, 6, 2, 6]
"""

from typing import List


def reverse(S: List[int], start: int, stop: int):
    """Reverse elements in implicit slice S[start: stop]."""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


S = [4, 3, 6, 2, 6]
reverse(S, start=0, stop=5)
print(S)


"""
start   stop        S
0       5           [6(4), 3, 6, 2, 4(6)]
1       4           [6, 2(3), 6, 3(2), 4]
2       3           条件不满足，不变

"""