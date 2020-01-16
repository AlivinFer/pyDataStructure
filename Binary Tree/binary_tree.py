# coding: UTF-8
# author: Fer
# date: 11/09/2019

class Node(object):
    def __init__(self, elem):
        self.val = elem
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        """向二叉树中添加节点"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        # 用队列来实现
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历（层次遍历）"""
        queue = [self.root]
        if queue is None:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre_order(self, node):
        """先序遍历（递归实现）：根 左 右"""
        if node is None:
            return
        print(node.val, end=" ")
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self, node):
        """中序遍历（递归实现）：左 根 右"""
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.val, end=" ")
        self.in_order(node.rchild)

    def post_order(self, node):
        """后序遍历（递归实现）：左 右 根"""
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.val, end=" ")


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.breadth_travel()
    print(" ")
    tree.pre_order(tree.root)
    print(" ")
    tree.in_order(tree.root)
    print(" ")
    tree.post_order(tree.root)
