class Solution:
    def getCount(self, root, k):
        levels = []

        def dfs(node, level):
            if node is None:
                return

            
            if node.left is None and node.right is None:
                levels.append(level)
                return

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)

        
        levels.sort()

        total = 0
        count = 0

        for cost in levels:
            if total + cost <= k:
                total += cost
                count += 1
            else:
                break

        return count