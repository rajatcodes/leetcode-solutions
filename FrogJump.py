# https://leetcode.com/problems/frog-jump/
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # as per problem setting if length of input is 2 or three and first three values aren't as below frog can't reach to the last stone
        if(stones==[0,1,3]) or (stones==[0,1,2]) or (stones==[0,1]):
            return True
        elif (len(stones) == 3) or (len(stones)==2):
            return False
        stone_possible_steps = {p : set() for p in range(len(stones))}
        stone_possible_steps[0].add(1)
        for p in range(1,len(stones)):
            for poss in stone_possible_steps[p-1]:
                if(stones[len(stones)-1]==stones[p-1]+poss):
                    return True;
                if (stones[p-1]+poss in stones) & (poss!=0):
                    stone_possible_steps[stones.index(stones[p-1]+poss)].update((poss-1, poss,poss+1))
        return False
