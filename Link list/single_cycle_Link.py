# -*- coding: UTF-8 -*-
# author: Fer
# date: 10/24/2019


class Node(object):
    def __init__(self, elem):
        self.val = elem
        self.next = None


# 单向循环链表
class singleCycleLink(object):
    def __init__(self, node=None):
        self.__head = node
        # 如果初始化是为非空链表，第一个节点要指向自己
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        count = 1
        cur = self.__head
        if self.is_empty():
            return 0
        else:
            while cur.next is not self.__head:
                count += 1
                cur = cur.next
        return count

    def travel(self):
        """遍历单向循环链表"""
        if self.is_empty():
            return None
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.val, end=" ")
            cur = cur.next
        # 退出循环时，cur指向尾节点，但尾节点的元素未打印
        print(cur.val)
        print("")

    def add(self, item):
        """链表头部插入元素（头插法）"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            # 因为是单向循环链表，构造完后还要指向自己
            node.next = node
        else:
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self, item):
        """链表尾部插入元素（尾插法）"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            count = 0
            prev = self.__head
            while count < pos-1:
                count += 1
                prev = prev.next
            node.next = prev.next
            prev.next = node

    def remove(self, item):
        """删除链表元素"""
        """
        需要考虑的情况蛮多
        1.只有一个节点时
        2.删除的是头节点
        3.删除的是中间节点
        4.删除的是尾节点
        """
        cur = self.__head
        prev = None
        while cur.next is not self.__head:
            if cur.val == item:
                if cur == self.__head:
                    # 删除的是头节点
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 删除的是中间节点
                    prev.next = cur.next
                return
            else:
                prev = cur
                cur = cur.next
        # 退出循环，指向尾节点
        if cur.val == item:
            # 只有一个节点时
            if cur == self.__head:
                self.__head = None
            else:
                prev.next = self.__head

    def search(self, item):
        """查找链表元素"""
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur.next is not self.__head:
                if cur.val == item:
                    return True
                else:
                    cur = cur.next
            # 退出循环，指向尾节点
            if cur.val == item:
                return True
            return False


# 测试
if __name__ == '__main__':
    ll = singleCycleLink()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.travel()

    ll.remove(1)
    ll.add(0)
    ll.travel()

    ll.insert(-2, 9)
    ll.travel()
    ll.insert(3, -7)
    ll.travel()
    ll.insert(7, 10)
    ll.travel()
    ll.remove(10)
    ll.travel()
    print(ll.search(3))
