def decode_message( s: str, p: str) -> bool:

# write your code here
        m, n = len(pattern), len(message)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for i in range(1, m + 1):
            if pattern[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
            else:
                break
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[i - 1] == message[j - 1] or pattern[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return dp[m][n]
  
        # return False
