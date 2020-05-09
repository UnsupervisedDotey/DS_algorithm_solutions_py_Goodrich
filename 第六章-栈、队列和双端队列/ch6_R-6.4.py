from ADT import ArrayStack


def recursive_remove(S: ArrayStack):
    if S.is_empty():
        pass
    else:
        S.pop()
        print(S._data)
        recursive_remove(S)


if __name__ == "__main__":
    s = ArrayStack()
    for i in range(10):
        s.push(i)

    print(s._data)
    recursive_remove(S=s)
