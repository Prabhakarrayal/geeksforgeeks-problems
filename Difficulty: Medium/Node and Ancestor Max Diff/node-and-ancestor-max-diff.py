class Solution:
    def maxDiff(self, root):
        ans = [-10**18]

        def dfs(node):
            if node is None:
                return float('inf')

            left_min = dfs(node.left)
            right_min = dfs(node.right)

            child_min = min(left_min, right_min)

        
            if child_min != float('inf'):
                ans[0] = max(ans[0], node.data - child_min)

            return min(node.data, child_min)

        dfs(root)
        return ans[0]