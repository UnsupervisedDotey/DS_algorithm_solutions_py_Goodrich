"""
对于一个含有n个元素的序列S，描述一个递归算法查找其最大值。所给出的递归算法时间复杂度和空间复杂度各是多少
"""

from typing import List


# 我的初始解答：传参子列表，基本情况只监视列表长度
def recursive_find_max(target: List[int]):
    if len(target) == 1:
        return target[0]
    else:
        return max(recursive_find_max(target[:-1]), target[-1])


print(recursive_find_max([1, 2, 3, 2, 1, 100]))

# 时间复杂度是 O(n)
# 空间复杂度是 O(1) ？ ×

# 卧槽GitHub上的某个答案说我的空间复杂度是O(n^2)？，因为我传参subarray也就是列表的一部分进递归，所以导致空间复杂度n平方！
# 不应该传 子列表 而应该传一个简单数字，比如index

"""
Running time is O(n)  (N calls to recursion, each taking O(1) time

Space is also O(n) since you have to call n activations
If I had passed in a copy of the subarray, it would have taken O(n^2) space, although if I had just passed
in the subarray (S[index:]), it should not have recopied it and still been O(n)
"""


# 我的优化解答？，传参只传index和list
# 等等 不是还是一样的要传list本身，外加一个index吗？还不如我的，只传一个子列表就行了。。。= =
def good_parameter_recursive_find_max(target_list: List[int], index: int):
    if index == len(target_list) - 1:
        return target_list[index]
    else:
        return max(good_parameter_recursive_find_max(target_list, index + 1), target_list[index])


print(good_parameter_recursive_find_max(target_list=[1, 2, 3, 2, 1, 100], index=0))
