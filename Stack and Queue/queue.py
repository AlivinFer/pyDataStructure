# coding: UTF-8
# author: Fer
# date: 10/31/2019

class Queue(object):
    def __init__(self):
        self.__list = []

    """进队和出队选择是从顺序表的尾部还是头部要具体看是经常进行入队还是出队"""
    def enqueue(self, item):
        """入队"""
        self.__list.append(item)

    def dequeue(self):
        """出队"""
        return self.__list.pop(0)  # pop（）函数删除对应下标元素并将其返回

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的长度"""
        return len(self.__list)


# 测试
if __name__ == '__main__':
    ll = Queue()
    print(ll.is_empty())
    ll.enqueue(1)
    ll.enqueue(2)
    ll.enqueue(3)
    ll.enqueue(4)
    print(ll.dequeue())
    print(ll.is_empty())
    print(ll.size())
    print(ll.dequeue())
    print(ll.dequeue())
    print(ll.dequeue())



