import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare root node
        if value < self.value:
            # if lesser go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # if something is already there, recursive
                self.left.insert(value)
        # value is greater go right of root
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

        # old code, refactored after watching lecture
        #     self.left = BinarySearchTree(value)
        # elif value >= self.value and self.right is None:
        #     self.right = BinarySearchTree(value)
        # elif value < self.value and self.left is not None:
        #     self.left.insert(value)
        # elif value >= self.value and self.right is not None:
        #     self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left is None:
            return False
        elif target >= self.value and self.right is None:
            return False
        elif target < self.value and self.left is not None:
            self = self.left
            return self.contains(target)
        elif target >= self.value and self.right is not None:
            self = self.right
            return self.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right is not None:
            self = self.right

        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        self.queue = Queue()
        self.queue.enqueue(node)

        while self.queue.len() > 0:
            node = self.queue.dequeue()
            if node.left:
                self.queue.enqueue(node.left)
            if node.right:
                self.queue.enqueue(node.right)
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        self.stack = Stack()
        self.stack.push(node)
        while self.stack.len() > 0:
            node = self.stack.pop()
            if node.left:
                self.stack.push(node.left)
            if node.right:
                self.stack.push(node.right)
            print(node.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)
