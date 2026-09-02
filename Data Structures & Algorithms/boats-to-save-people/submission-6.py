class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l=0
        boat=0
        r=len(people)-1
        people.sort()
        boat=0
        while l<r:
            sum=people[l]+people[r]
            if sum<=limit:
                people.pop(r)
                people.pop(l)
                r-=2
                boat+=1
            elif sum>limit:
                r-=1
        boat+=len(people)
        return boat
