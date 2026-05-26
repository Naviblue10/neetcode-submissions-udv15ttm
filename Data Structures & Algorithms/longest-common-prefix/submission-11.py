class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=list(strs[0])
        temp=[]
        for i in range(1,len(strs)):
            if strs[i]=="":
                common=""
                break
            temp=[]
            last_indx=len(common) if len(common)<len(strs[i]) else len(strs[i])
            for j in range(last_indx):
                if common[j]==strs[i][j]:
                    temp.append(common[j])
                else:
                    common=temp
                    break
            common=temp
        return ''.join(common)

