# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.max_prod = 0

        # Step 1: Compute total sum of the tree
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)

        # Step 2: Compute subtree sums and maximize product
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            subtree_sum = node.val + left + right

            # product if we cut above this subtree
            self.max_prod = max(
                self.max_prod,
                subtree_sum * (total - subtree_sum)
            )

            return subtree_sum

        dfs(root)
        return self.max_prod % MOD

        