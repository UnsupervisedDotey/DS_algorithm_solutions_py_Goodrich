from ADT import ArrayStack


class Solution:
    def transfer(self, S: ArrayStack, T: ArrayStack):
        while True:
            try:
                T.push(S.pop())
            except:
                break


if __name__ == "__main__":
    s = ArrayStack()
    t = ArrayStack()
    for i in range(10):
        s.push(i)

    sol = Solution()
    sol.transfer(S=s, T=t)
    print(t._data)
