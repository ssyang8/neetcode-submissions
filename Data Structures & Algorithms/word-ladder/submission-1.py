class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                adj[key].append(word)
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            sz = len(q)
            for _ in range(sz):
                (word, res) = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    key = word[:i] + '*' + word[i+1:]
                    for neighbor in adj[key]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append((neighbor, res + 1))
        
        return 0

        