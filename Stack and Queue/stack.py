# coding: UTF-8
# author: Fer
# date: 10/31/2019

class Stack(object):
    def __init__(self):
        # 采用的是顺序表存储
        self.__list = []

    def push(self, item):
        """元素进栈"""
        self.__list.append(item)  # 从顺序表的尾部插入，时间复杂度为O（1）

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def size(self):
        """栈的长度"""
        return len(self.__list)


# 测试
if __name__ == '__main__':
    ll = Stack()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    print(ll.pop())
    print(ll.size())
    print(ll.pop())
    print(ll.pop())
    print(ll.pop())
