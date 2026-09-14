class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l=1
        r=piles[-1]
        res=r
        while l<=r:
            hours=0
            k=(l+r)//2
            for i in piles:
                hours+=-(-i//k)
            if hours>h:
                l=k+1
            elif hours<=h:
                r=k-1
                res=min(res,k)
            else:
                return res
            
        return res

            
