# Polygons
# The goal of this exercise is to provide an OOP implementation of a binary search tree.

# Binary Search Tree
# In computer science, a tree is a data type that simulates a tree structure, with a root value and subtrees of children. Each node contains a value.

# example

# A binary search tree is a special type of tree, which respect the following properties:

# Every node has at most two children
# The left subtree of a node contains only nodes with keys lesser than the node’s key
# The right subtree of a node contains only nodes with keys greater than the node’s key
# example2

# Part 1: The Binary Tree
# Let’s start by implementing a representation of a binary tree (a tree where every node has at most two children), a tree is represented by its root node.
# Create a class Node, it has three attributes, left, right and value, respectively its left and right child and its value, the children can be None.
# Then add the basic methods to this class: get_left(), get_right(), set_left(node), set_right(node), set_value(value) and get_value().

# Part 2: The Binary Search Tree
# Now let’s transform this binary tree into a binary search tree, implement a function add_node(node) and add it to the three, make sure you respect all the conditions of the binary search tree (the node needs to be added at the right place, depending on its value).

# Part 3: Use The Binary Search Tree
# Implement a method search(value) which return the node containing this value inside the tree.