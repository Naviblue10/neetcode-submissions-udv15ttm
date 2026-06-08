class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length=len(word1) if len(word1)<len(word2) else len(word2)
        i=0
        new_word=""
        while i<length:
            new_word+=word1[i]+word2[i]
            i+=1
        new_word+=word2[i:]
        new_word+=word1[i:]
        return new_word
        