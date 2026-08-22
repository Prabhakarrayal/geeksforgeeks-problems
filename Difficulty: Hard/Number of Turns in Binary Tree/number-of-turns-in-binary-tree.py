class Solution:
    def numberOfTurns(self, root, p, q):

        def find_path(node, target, path):
            if not node:
                return False

            if node.data == target:
                return True

            path.append('L')
            if find_path(node.left, target, path):
                return True
            path.pop()

            path.append('R')
            if find_path(node.right, target, path):
                return True
            path.pop()

            return False

        def lca(node, a, b):
            if not node or node.data == a or node.data == b:
                return node

            left = lca(node.left, a, b)
            right = lca(node.right, a, b)

            if left and right:
                return node

            return left if left else right

        ancestor = lca(root, p, q)

        path_p = []
        path_q = []

        find_path(ancestor, p, path_p)
        find_path(ancestor, q, path_q)

    # Travel from p -> LCA
        path_p.reverse()

    # Complete path from p -> q
        path = path_p + path_q

        turns = 0

        for i in range(1, len(path)):
            if path[i] != path[i - 1]:
                turns += 1

        return turns if turns > 0 else -1