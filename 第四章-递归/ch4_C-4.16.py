"""
编写一个简短的递归Python函数， 它接受一个字符串 s 并且输出其逆置字符串。
例如：字符串 'pots&pans' 的逆置字符串为 'snap&stop'。
"""


def recursive_reverse(texts: str, index: int):
    """输出其逆置字符串

    :param texts: 字符串
    :param index: 定位
    :return: 字符串的逆置字符串 一开始为空字符串，慢慢变大，装逆置结果

    时间复杂度： O(n)
    空间复杂度： O(1)

    """
    if index == len(texts) - 1:
        return texts[-1]
    else:
        return recursive_reverse(texts, index+1) + texts[index]


print(recursive_reverse('pots&pans', 0))
