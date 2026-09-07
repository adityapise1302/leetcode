class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for c in key:
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = TrieNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.value = val

    def sum(self, prefix: str) -> int:
        res = 0
        curr = self.root
        for c in prefix:
            if not curr.children[ord(c) - ord('a')]:
                return 0
            curr = curr.children[ord(c) - ord('a')]
        q = [curr]
        while q:
            curr = q.pop()
            res += curr.value
            for c in curr.children:
                if c:
                    q.append(c)
        return res
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)