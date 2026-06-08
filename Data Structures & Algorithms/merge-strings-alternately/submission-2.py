class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length=len(word1) if len(word1)<len(word2) else len(word2)
        i=0
        new_word=""
        while i<length:
            new_word+=word1[i]+word2[i]
            i+=1
        rem_word=word2 if len(word1)<len(word2) else word1
        new_word+=rem_word[i:]
        return new_word
        