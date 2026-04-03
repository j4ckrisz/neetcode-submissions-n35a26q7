class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        import numpy as np  

        letters = []
        words = []
        groups = []

        for i in range(len(strs)):
            for j in range(len(strs[i])):          
                letters.append(strs[i][j])
            letters.sort()                          
            words.append("".join(letters))          
            letters.clear()                         

        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue
            current_group = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if not used[j] and words[j] == words[i]:
                    current_group.append(strs[j])
                    used[j] = True
            groups.append(current_group)

        return groups