class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        dics = {}
        dictt = {}

        for ch in s: 
            if ch not in dics: 
                dics[ch] = 0

            dics[ch] += 1

        for ch in t: 
            if ch not in dictt: 
                dictt[ch] = 0

            dictt[ch] += 1

        return dics == dictt

        