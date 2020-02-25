"""
绘制函数 PuzzleSolve(3, S, U)（代码段4-14）执行的递归追踪，其中 S 为空并且 U = {a, b, c, d}。

"""

from typing import List, Set


# --------------R4-5------------------------
# Note that S is our attempt at solving the sequence and U is our set of all possible numbers that are unused
def solves(S):
    # Note, this is a random solution to the pseudoproblem
    return S == ['d', 'b', 'c']


# 穷举法（枚举法）
def PuzzleSolver(k: int, S: List[int], U: Set):
    for e in sorted(U).copy():
        # 放一个u进空列表
        S.append(e)
        U.remove(e)
        if k == 1:          # 基本情况，还只进不出 只用判断，不用返回值
            print(S)
            if solves(S):
                print(f'Solution found: {S}')
        else:
            PuzzleSolver(k - 1, S, U)

        # 把列表里一个u拿出来，放回集合U
        # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        # list.pop([index=-1])
        U.add(S.pop())      # removes the last item of an array


"""
Note: It would be very difficult to draw the entire recursive trace so I'm outputting the order of the calls

Also note: a set is unordered, so the order in which you would get these outputs is not guaranteed.
I have ordered the set for this example

PuzzleSolver(3, [], {'a','b','c','d'})
    PuzzleSolver(2, [a], {'b','c','d'})
        PuzzleSolver(1, ['a','b'], {'c','d'})
            Tests ['a','b','c'] and ['a', 'b', 'd'] and returns None
        PuzzleSolver(1, ['a','c'], {'b','d'})
            Tests ['a', 'c', 'b'] and ['a','c','d'] then returns None

        .....


    PuzzleSolver(2, [b], {'a','c','d'})
        ....

    PuzzleSolver(2, [c], {'a','b','d'})

        ...
    PuzzleSolver(2, [d], {'a','b','c'})
        ...

        PuzzleSolver(1, ['d','c'], {'a','b'})
            Tests ['d', 'c', 'a'] and ['d','c','b'] then returns None



"""

PuzzleSolver(3, [], {'a', 'b', 'c', 'd'})
