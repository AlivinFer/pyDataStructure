# coding: UTF-8
# author: Fer
# date: 11/26/2018

class Sort(object):
    def __init__(self):
        pass

    def bubble_sort(self, a: list):
        """冒泡排序"""
        length = len(a)
        for i in range(length - 1, 0, -1):
            count = 0  # 用来记录元素交换次数
            for j in range(0, i):
                """优化: 当没有发生交换时，元素已有序"""
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    count += 1
            if count == 0:
                break
        return a

    def choose_sort(self, a: list):
        """选择排序"""
        length = len(a)
        for i in range(length-1, 0, -1):
            index = 0
            max_value = a[index]
            for j in range(1, i+1):
                if max_value < a[j]:
                    index = j
                    max_value = a[index]
            a[i], a[index] = a[index], a[i]
            # print(a)
        return a

    def insert_sort(self, a: list):
        """插入排序"""
        for i in range(1, len(a)):
            for j in range(i, 0, -1):
                if a[j] < a[j-1]:
                    a[j], a[j-1] = a[j-1], a[j]
        return a

    def shell_sort(self, a: list):
        """希尔排序"""
        n = len(a)
        gap = n // 2  # python3中取整的话用//
        while gap >= 1:
            # 插入算法，与普通的插入算法的区别就是gap的步长
            for i in range(gap, n):
                j = i
                while j > 0:
                    if a[j] < a[j-gap]:
                        a[j], a[j-gap] = a[j-gap], a[j]
                        j -= gap
                    else:
                        break
            gap //= 2
        return a

    def quick_sort(self, a: list, first: int, last: int):
        """快排（分治法）"""
        # 终止条件
        if first >= last:
            return
        low = first
        high = last
        mid_value = a[low]  # 以首元素作为主元
        while low < high:
            while low < high and a[high] >= mid_value:
                # 左移，找到一个不大于主元的值
                high -= 1
            a[low] = a[high]
            while low < high and a[low] < mid_value:
                # 右移，找到一个大于主元的值
                low += 1
            a[high] = a[low]
        # 循环退出时，low == high
        a[low] = mid_value

        # 递归调用，对mid_value两边的元素进行快排
        self.quick_sort(a, first, low-1)
        self.quick_sort(a, low+1, last)

        return a

    def merge_sort(self, a: list):
        """合并排序(分治法)"""
        n = len(a)
        if n <= 1:
            return a
        mid = n // 2
        # 用递归将原序列进行拆分
        left_li = self.merge_sort(a[:mid])
        right_li = self.merge_sort(a[mid:])

        # 将子序列进行合并
        left_pointer, right_pointer = 0, 0
        # 生成一个新的序列,需要开辟新的空间来存储
        result = []
        while left_pointer < len(left_li) and right_pointer < len(right_li):
            if left_li[left_pointer] <= right_li[right_pointer]:
                result.append(left_li[left_pointer])
                left_pointer += 1
            else:
                result.append(right_li[right_pointer])
                right_pointer += 1
        result += left_li[left_pointer:]
        result += right_li[right_pointer:]
        return result


if __name__ == '__main__':
    test = Sort()
    a1 = [9, 0, 1, 7, 2, 7, 3, 10, 0, 5]
    # print(test.bubble_sort(a1))
    # print(test.choose_sort(a1))
    # print(test.insert_sort(a1))
    # print(test.shell_sort(a1))
    # print(test.quick_sort(a1, 0, len(a1)-1))
    print(test.merge_sort(a1))

