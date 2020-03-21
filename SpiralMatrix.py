# https://leetcode.com/problems/spiral-matrix-ii/
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        a = [[0]*n for i in range(n)]
        end = n
        begin=0
        val=1
        while(val<(n**2)+1):
            for i in range(begin,end):
                a[begin][i]=val
                val = val+1
            for i in range(begin+1,end):
                a[i][end-1]=val
                val = val+1
            for i in reversed(range(begin,end-1)):
                a[end-1][i]=val
                val = val+1
            for i in reversed(range(begin+1,end-1)):
                a[i][begin]=val
                val = val+1
            begin = begin + 1
            end = end-1
        return a
