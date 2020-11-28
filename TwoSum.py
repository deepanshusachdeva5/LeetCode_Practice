class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_dict = {} #key : (count,index)
        ind= 0
        for n in nums:
            if n in all_dict.keys():
                all_dict[n] = (all_dict[n][0]+1,ind)
            else:
                all_dict[n] = (1,ind)
            ind+=1
            
        ans = []
        c=0
        for n in nums:
            if (target-n) in all_dict.keys():
                if target-n == n:
                    if all_dict[target-n][0] >1:
                        ans = [c,all_dict[target-n][1]]
                        break
                        
                else:
                    ans = [c,all_dict[target-n][1]]
                    break
            c+=1
                    
        return ans
