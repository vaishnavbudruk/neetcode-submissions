class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        ans=[]
        count=0
        for i in range(0,len(nums)):
            if nums[i]!=0: mul=mul*nums[i]
            if nums[i]==0: count+=1
        print("count zero: ",count)
        for i in range(0,len(nums)):
            if count>1: ans.append(int(0))
            elif(count==1):
                if nums[i]==0:
                    ans.append(int(mul))
                else:
                    ans.append(int(0))
            else:
                ans.append(int(mul/nums[i]))
        return ans