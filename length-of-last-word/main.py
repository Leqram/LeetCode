class Solution():
    def lengthOfLastWord(self, s: str) -> int:
        list_word = s.split()
        last_word = list_word[-1]
        return len(last_word)



sol = Solution()

print(sol.lengthOfLastWord("   fly me   to   the moon  "))