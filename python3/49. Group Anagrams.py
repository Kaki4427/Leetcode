# method1 87/95
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ordered = dict()
        for word in strs:
            oword = self.orderword(word)
            if oword not in ordered:
                ordered[oword] = [word]
            else:
                ordered[oword].append(word)
        return list(ordered.values())

    def orderword(self, word):
        word = list(word)
        word = sorted(word)
        return "".join(word)
