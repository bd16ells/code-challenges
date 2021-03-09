# Short Encoding of Words
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3662/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        encoded = ""
        indices = []
        words = sorted(words, key=lambda x: len(x), reverse=True)
        for word in words:
            if encoded == "":
                encoded += word + "#"
                indices.append(0)
                continue

            if encoded.find(word + "#") == -1:
                indices.append(len(encoded))
                encoded = encoded + word + "#"
            else:
                indices.append(encoded.find(word))
        return(len(encoded))