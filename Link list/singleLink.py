# 构建节点
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


# 构建单链表
class singleLinkList(object):
    def __init__(self, node=None):  # 初始化时，先创建一个空链表
        self.__head = node  # __head表示私有变量，只作用于类的内部

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # 游标（类似于指针），用来移动遍历节点
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")  # 这样可以不换行
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部增加元素(头插法)"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部增加元素（尾插法）"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < pos-1:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """在链表中查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


# 测试
if __name__ == '__main__':
    # 创建一个单链表对象
    ll = singleLinkList()
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