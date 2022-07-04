class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapStoT = {}
        mapTtoS = {}
        for i in range(len(t)):
            if (s[i] in mapStoT and mapStoT[s[i]] != t[i]) or (t[i] in mapTtoS and mapTtoS[t[i]] != s[i]):
                return False
            mapStoT[s[i]] = t[i]
            mapTtoS[t[i]] = s[i]
        return True
