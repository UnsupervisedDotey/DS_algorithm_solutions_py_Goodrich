from ADT import ArrayStack
from typing import List


def reverse_list_by_stack(l: List, s: ArrayStack):
    for i in l:
        s.push(i)

    for i in range(len(l)):
        if s.is_empty():
            break
        else:
            l[i] = s.pop()

    return l


if __name__ == "__main__":
    s = ArrayStack()
    l = [i for i in range(10)]
    l = reverse_list_by_stack(l, s)
    print(l)
