"""
给出一个算术表达式中，分组符号匹配的精确完整定义
"""
from ADT import ArrayStack


def kuo_hao_match(expr: str):
    """返回True 如果所有的delimiters 都前后正确匹配，反之返回False"""
    left = '([{'
    right = ')]}'
    happened = ArrayStack()
    for _chr in expr:
        if _chr in left:
            happened.push(_chr)
            
        elif _chr in right:
            if happened.is_empty():
                return False
            if right.index(_chr) != left.index(happened.pop()):
                return False

    # 如果能顺利遍历排空所有happened，则返回True
    return happened.is_empty()


if __name__ == "__main__":
    print(kuo_hao_match('((1+1)*[1+3])'))
