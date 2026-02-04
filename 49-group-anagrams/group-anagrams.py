class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramListsHash = dict()
        for word in strs:
            temp_chars = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                temp_chars[idx] += 1
            temp_tuple = tuple(temp_chars)
            anagramListsHash.setdefault(temp_tuple, []).append(word)
        return list(anagramListsHash.values())
