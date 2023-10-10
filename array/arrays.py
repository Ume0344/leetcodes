from typing import List

class Array:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = len(strs)
        temp = strs.copy() # copy method will not change the origional string (strs)
        dic ={}

        for i in range(l):
            temp[i] = str(''.join(sorted(temp[i])))
            if temp[i] not in dic:
                dic[temp[i]] = [strs[i]]
            else:
                dic[temp[i]].append(strs[i])
        
        return list(dic.values())
