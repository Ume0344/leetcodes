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

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        dic = {}
        lis = []

        for i in range(l):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]]+=1
        # key takes the each element in dic.item() and pass to lambda function
        sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            lis.append(sorted_dic[i][0])
        
        return lis
