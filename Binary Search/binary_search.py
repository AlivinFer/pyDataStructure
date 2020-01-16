# coding : UTF-8
# author: Fer
# date: 1/15/2020

# 前提：有序的列表
def binary_search(a: list, item: int):
    """二分查找（递归）"""
    n = len(a)
    if n > 0:
        mid = n // 2
        if a[mid] == item:
            return True
        elif a[mid] > item:
            return binary_search(a[:mid], item)
        else:
            return binary_search(a[mid:], item)
    return False

def binary_search2(a: list, item: int):
    """二分查找（非递归）"""
    first = 0
    last = len(a)-1
    mid = (first+last) // 2
    while first <= last:
        if a[mid] == item:
            return True
        elif a[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    s1 = [1, 2, 3, 5, 6, 8, 9, 10, 11]
    print(binary_search(s1, 2))
