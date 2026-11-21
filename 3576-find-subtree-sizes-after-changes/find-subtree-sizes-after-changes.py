class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_children = [[] for _ in range(n)]

        stack = {}
        order = []

        # DFS on original tree
        dfs = [(0, False)]

        while dfs:
            node, exit_flag = dfs.pop()

            ch = s[node]

            if exit_flag:
                stack[ch].pop()
                continue

            # Find closest ancestor with same character
            if ch in stack and stack[ch]:
                new_parent = stack[ch][-1]
            else:
                new_parent = parent[node]

            if node != 0:
                new_children[new_parent].append(node)

            stack.setdefault(ch, []).append(node)

            order.append(node)

            dfs.append((node, True))

            for child in reversed(children[node]):
                dfs.append((child, False))

        # Calculate subtree sizes
        ans = [1] * n

        for node in reversed(order):
            for child in new_children[node]:
                ans[node] += ans[child]

        return ans