class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % 1000

        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.buckets[index].append([key, value])

    def get(self, key: int) -> int:
        index = key % 1000

        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key: int) -> None:
        index = key % 1000

        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                self.buckets[index].pop(i)
                return