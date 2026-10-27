from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            state, steps = queue.popleft()

            if state == target:
                return steps

            for i in range(4):
                for delta in (-1, 1):
                    digit = (int(state[i]) + delta) % 10
                    nxt = state[:i] + str(digit) + state[i + 1:]

                    if nxt in dead or nxt in visited:
                        continue

                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

        return -1