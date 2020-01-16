# -*- coding: UTF-8 -*-
# author: Fer
# date: 10/17/2019


# 构建节点
class Node(object):
    def __init__(self, item):
        self.val = item
        self.prev = None
        self.next = None


# 构建双链表
class DLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断双链表是否为空"""
        return self.__head is None

    def length(self):
        """双链表长度"""
        count = 0
        cur = self.__head
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历双链表"""
        cur = self.__head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print('')

    def add(self, elem):
        """双链表头部增加元素（头插法）"""
        node = Node(elem)
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def append(self, elem):
        """双链表尾部增加元素（尾插法）"""
        node = Node(elem)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, elem):
        """在指定位置(从0开始)插入元素"""
        if pos <= 0:
            self.add(elem)
        elif pos > self.length() - 1:
            self.append(elem)
        else:
            count = 0
            node = Node(elem)
            cur = self.__head
            while count < pos:
                count += 1
                cur = cur.next
            node.prev = cur.prev
            node.next = cur
            cur.prev.next = node
            cur.prev = node

    def remove(self, elem):
        """删除节点"""
        cur = self.__head
        while cur:
            if cur.val == elem:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """在双链表中查找节点是否存在"""
        cur = self.__head
        while cur:
            if cur.val == item:
                return True
            else:
                cur = cur.next
        return False


# 测试
if __name__ == '__main__':
    ll = DLinkList()
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
