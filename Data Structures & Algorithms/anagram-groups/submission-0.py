class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            x="".join(sorted(word))

            if x not in hashmap:
                hashmap[x]=[]

            hashmap[x].append(word)

        return list(hashmap.values())

        