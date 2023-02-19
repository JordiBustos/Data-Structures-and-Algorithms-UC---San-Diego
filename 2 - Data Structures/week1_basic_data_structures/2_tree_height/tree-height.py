# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_index):
        self.children.append(child_index)
               

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def __createTree(self):
                nodes = [Node(i) for i in range(self.n)] 
                
                for i in range(self.n):
                        if self.parent[i] == -1:
                                self.root = i
                        else:
                                nodes[self.parent[i]].add_child(nodes[i])
                        
                return nodes

        def compute_height(self):
                # Replace this code with a faster implementation
                tree = self.__createTree()
                d = deque()

                d.append(tree[self.root])
                height = 0

                while len(d):
                        height += 1
                        for i in range(len(d)):
                                node = d.popleft()

                                for child in node.children:
                                        d.append(child)

                return height 

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
