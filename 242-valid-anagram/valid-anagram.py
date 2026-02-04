class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable = dict()
        if len(s) != len(t):
            return False
        for char in s:
            hashTable[char] = hashTable.get(char, 0) + 1
        for char in t:
            if hashTable.get(char, 0) > 0:
                hashTable[char] -= 1
            else:
                return False
        for key, val in hashTable.items():
            if val != 0:
                return False
        return True
