def decode_message(s: str, p: str) -> bool:
    memo = {}
    def dfs(s_index, p_index):
        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]
        if s_index == len(s) and p_index == len(p):
            return True
        if p_index == len(p):
            return False
        if s_index == len(s):
            while p_index < len(p) and p[p_index] == '*':
                p_index += 1
            return p_index == len(p)
        if p[p_index] == s[s_index] or p[p_index] == '?':
            result = dfs(s_index + 1, p_index + 1)      
        elif p[p_index] == '*':
            result = dfs(s_index, p_index + 1) or dfs(s_index + 1, p_index)
        else:
            result = False
        memo[(s_index, p_index)] = result
        return result
    return dfs(0, 0)
