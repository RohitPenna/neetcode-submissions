class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        components = n

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]

            return node

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            # Attach the smaller group to the larger group.
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return True

        for a, b in edges:
            if union(a, b):
                components -= 1

        return components