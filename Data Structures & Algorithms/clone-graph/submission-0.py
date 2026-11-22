"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mp = {}
        def dfs(node):

            if node in mp:
                return mp[node]
            newNode = Node(node.val)
            mp[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode
        return dfs(node)
                
            