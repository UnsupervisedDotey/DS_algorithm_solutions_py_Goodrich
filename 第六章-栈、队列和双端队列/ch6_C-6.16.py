class Empty(Exception):
    pass


class StackFull(Exception):
    pass


class ArrayStack:
    def __init__(self, max_len: int = None):
        self._data = []
        self._max_len = max_len

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        if self._max_len == len(self._data):
            raise StackFull("Stack is full")

        self._data.append(e)
        print(self._data)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()  # 我靠( ‵o′)凸，此pop是list里自带的pop，而不是我自己写的pop()


if __name__ == "__main__":
    s = ArrayStack(max_len=3)
    for i in range(4):
        s.push(i)
