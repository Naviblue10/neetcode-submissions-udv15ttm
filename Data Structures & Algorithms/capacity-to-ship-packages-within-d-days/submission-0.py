class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res=r
        while(l<=r):
            m=(l+r)//2
            load=0
            day=1
            for i in weights:
                if (load+i<=m):
                    load+=i
                else:
                    day+=1
                    load=i
            if day<=days:
                r=m-1
                res=min(res,m)
            elif day>days:
                l=m+1
        return res