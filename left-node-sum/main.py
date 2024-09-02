import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves(root: TreeNode) -> int:
    # This function should be implemented elsewhere.
    value = 0
    if root:
        if root.left:
            if is_leaf(root.left):
                value = root.left.val
        return value + sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)
    return value

def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None

class TestSumOfLeftLeaves(unittest.TestCase):
    def test_basic(self):
        root = TreeNode(3, 
                        TreeNode(9), 
                        TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(sum_of_left_leaves(root), 24)

    def test_multiple_leaves(self):
        root = TreeNode(1, 
                        TreeNode(2, TreeNode(4), TreeNode(5)),
                        TreeNode(3, None, TreeNode(6)))
        self.assertEqual(sum_of_left_leaves(root), 4)

    def test_empty_tree(self):
        root = None
        self.assertEqual(sum_of_left_leaves(root), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(sum_of_left_leaves(root), 0)

    def test_only_left_children(self):
        root = TreeNode(1, 
                        TreeNode(2, 
                                 TreeNode(3, 
                                          TreeNode(4))))
        self.assertEqual(sum_of_left_leaves(root), 4)

    def test_only_right_children(self):
        root = TreeNode(1, 
                        None, 
                        TreeNode(2, 
                                 None, 
                                 TreeNode(3)))
        self.assertEqual(sum_of_left_leaves(root), 0)

    def test_balanced_tree(self):
        root = TreeNode(10, 
                        TreeNode(5, 
                                 TreeNode(2), 
                                 TreeNode(8)), 
                        TreeNode(15, 
                                 None, 
                                 TreeNode(7)))
        self.assertEqual(sum_of_left_leaves(root), 2)

    def test_same_value_nodes(self):
        root = TreeNode(1, 
                        TreeNode(1, 
                                 TreeNode(1)), 
                        TreeNode(1))
        self.assertEqual(sum_of_left_leaves(root), 1)

    def test_larger_tree(self):
        root = TreeNode(5, 
                        TreeNode(3, 
                                 TreeNode(1), 
                                 TreeNode(4)), 
                        TreeNode(8, 
                                 TreeNode(6), 
                                 TreeNode(9)))
        self.assertEqual(sum_of_left_leaves(root), 7)

    def test_complex_tree(self):
        root = TreeNode(7, 
                        TreeNode(3, 
                                 TreeNode(1, 
                                          TreeNode(0, 
                                                   TreeNode(-1))), 
                                 TreeNode(2)), 
                        TreeNode(9, 
                                 TreeNode(8), 
                                 TreeNode(10)))
        self.assertEqual(sum_of_left_leaves(root), 7)

if __name__ == "__main__":
    unittest.main()
