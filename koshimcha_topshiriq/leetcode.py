class Solution:
    def lengthOfLastWord(self, s: str):
        print(len(s.split()[-1]))


s = Solution()
s.lengthOfLastWord(s="   fly me   to   the moon  ")
s.lengthOfLastWord(s="luffy is still joyboy")
