#https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [[0]*(n+1) for i in range(n+1)]
        print(dp)
        if(n==0):
            return 0
        dp[n-1][n]=1
        if n>=2:
            dp[n-2][n]=2
        for s in reversed(range(n-1)):
            dp[s-1][n]=dp[s][n]+dp[s+1][n]
        return dp[0][n]
            
            
