# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/22 4:47 下午
@Auth ： Codewyf
@File ：BinearySearchTree.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class OperationTree:
    def insert(self, root, val):
        if root == None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def query(self, root, val):
        if root == None:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.query(root.left, val)
        elif val > root.val:
            return self.query(root.right, val)

    def findMin(self, root):
        if root.left:
            return self.findMin(root.left)
        else:
            return root

    def findMax(self, root):
        if root.right:
            return self.findMax(root.right)
        else:
            return root

    def delNode(self, root, val):
        if root == None:
            return
        if val < root.val:
            root.left = self.delNode(root.left, val)
        elif val > root.val:
            root.right = self.delNode(root.right, val)
        # 当val == root.val时，分三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
        else:
            if root.left and root.right:
                #既有左子树又有右子树，则需要找到右子树中最小值节点
                temp = self.findMin(root.right)
                root.val = temp.val
                #再把右子树中最小值节点删除
                root.right = self.delNode(root.right, temp.val)
            elif root.left == None and root.right == None:
                #左右子树都为空
                root = None
            elif root.left == None:
                #只有右子树
                root = root.right
            elif root.right == None:
                #只有左子树
                root = root.left
        return root

    def printTree(self, root):
        #打印BST
        if root == None:
            return
        self.printTree(root.left)
        print(root.val, end = ' ')
        self.printTree(root.right)

if __name__ == '__main__':
    List = [17, 5, 35, 2, 11, 29, 38, 9, 16, 9]
    root = None
    op = OperationTree()
    for val in List:
        root = op.insert(root, val)
    print('中序遍历打印BST: ', end = ' ')
    op.printTree(root)
    print(' ')
    print('根节点的值为：', root.val)
    print('树中最大的节点为: ', op.findMax(root).val)
    print('树中最小的节点为:' , op.findMin(root).val)
    print('查询树中值为5的节点:', op.query(root, 5))
    print('查询树中值为100的节点:', op.query(root, 100))
    print('删除树中值为16的节点: ', end = ' ')
    root = op.delNode(root, 16)
    op.printTree(root)
    print(' ')
    print('删除树中值为5的节点: ', end = ' ')
    root= op.delNode(root, 5)
    op.printTree(root)
    print(' ')


