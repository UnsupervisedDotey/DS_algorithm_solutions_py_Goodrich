"""
编写一个简短的递归Python函数，确定一个字符串 s 是否是它的一个回文字符串，也就是说，该字符串与其逆置字符串相同。
例如，字符串 'rececar' 和 'gohangasalamiimalasagnahog' 是否是回文字符串
"""


# 时间复杂度 O(n) ，虽然只执行 小于等于 n/2 次；空间复杂度 O(1)


def recursive_plalindrome(text: str, half_index: int = 0):
    """递归判断，是否是回文"""

    if half_index > 0.5 * len(text):
        return True
    else:
        return [False, True][recursive_plalindrome(text, half_index + 1) * (text[half_index] == text[-1 - half_index])]


print(recursive_plalindrome(text='rececar'))
print(recursive_plalindrome(text='gohangasalamiimalasagnahog'))

# 办法1：沿用逆置函数，与自身比较
# def recursive_reverse(texts: str, index: int):
#     """输出其逆置字符串
#
#     :param texts: 字符串
#     :param index: 定位
#     :return: 字符串的逆置字符串 一开始为空字符串，慢慢变大，装逆置结果
#
#     时间复杂度： O(n)
#     空间复杂度： O(1)
#
#     """
#     if index == len(texts) - 1:
#         return texts[-1]
#     else:
#         return recursive_reverse(texts, index+1) + texts[index]
#
#
# def check_plalindrome(text: str):
#
#     return recursive_reverse(text, 0) == text
#
#
# print(check_plalindrome('pots&pans'))
# print(check_plalindrome('gohangasalamiimalasagnahog'))
