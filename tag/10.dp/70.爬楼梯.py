#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:return n
        dp = [0 for x in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            #dp[i]为爬到i级台阶的方案书
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
# @lc code=end

