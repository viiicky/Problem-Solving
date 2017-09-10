package com.company;

/* A Binary Tree node */
class Node {
    int data;
    Node left, right;

    Node(int item) {
        data = item;
        left = right = null;
    }
}

/**
 * Given a Binary Tree, convert it into its mirror.
 * Time Complexity: O(n) where n is number of nodes present in the tree.
 *
 * Problem Link: http://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/
 */
class MirrorTree {
    void mirror(Node node) {
        // Your code here
        if (node == null) {
            return;
        }

        Node temp = node.left;
        node.left = node.right;
        node.right = temp;
        mirror(node.left);
        mirror(node.right);
    }
}
