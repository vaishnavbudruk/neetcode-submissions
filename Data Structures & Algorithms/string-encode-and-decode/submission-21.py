class Solution:

    def encode(self, strs: List[str]) -> str:
        st=""
        for i in strs:
            st=st+str(len(i))+'|'+i
        # print(st)
        return st
        

    def decode(self, s: str) -> List[str]:
        ans=[]
        nums=[]
        c=""
        count=""
        nums=['0','1','2','3','4','5','6','7','8','9']
        i=0
        while i <len(s):
            while s[i] in nums:
                count=count+s[i]
                i=i+1
            # print("count",count,"i",i)
            if s[i]=='|': i=i+1
            # print("i after |",i)
            num=int(count)
            k=""
            while num>0 and i<len(s):
                # print("num",num,"i",i,"character",s[i])
                k=k+s[i]
                num-=1
                i+=1
            ans.append(k)
            count=""
            
        return ans




