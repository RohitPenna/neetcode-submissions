from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        queue = deque([node])

        clones = {}
        clones[node] = Node(node.val)

        while queue:
            x = queue.popleft()

            for i in x.neighbors:

                if i not in clones:
                    clones[i] = Node(i.val)
                    queue.append(i)

                clones[x].neighbors.append(clones[i])

        return clones[node]