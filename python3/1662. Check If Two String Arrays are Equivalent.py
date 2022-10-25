# method1 58/76
def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    s1 = ""
    s2 = ""
    for s in word1:
        s1 += s
    for s in word2:
        s2 += s
    return s1 == s2

# method2 97/76
def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    word1 = "".join(word1)
    word2 = "".join(word2)
    return word1 == word2

# method3 58/76
def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    for c1, c2 in zip(self.generate(word1), self.generate(word2)):
        if c1 != c2:
            return False
    return True

def generate(self, wordlist: List[str]):
    for word in wordlist:
        for char in word:
            yield char
    yield None
