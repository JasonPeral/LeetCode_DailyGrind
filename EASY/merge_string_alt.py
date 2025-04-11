class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        tracking = ''
        x1 = len(word1)
        y1 = len(word2)

        if x1 < y1:
            for x, char in enumerate(word1):

                tracking += word1[x]
                tracking += word2[x]
            tracking += word2[x1: y1]
        
        else:
            for x, char in enumerate(word2):
                tracking += word1[x]
                tracking += word2[x]
            tracking += word1[y1: x1]

        return tracking
    
    # Tests
def run_tests():
    s = Solution()
    test_cases = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("", "abc", "abc"),
        ("abc", "", "abc"),
        ("a", "b", "ab"),
        ("abc", "defgh", "adbecfgh"),
    ]
    
    for i, (word1, word2, expected) in enumerate(test_cases):
        result = s.mergeAlternately(word1, word2)
        assert result == expected, f"Test case {i+1} failed: expected '{expected}', got '{result}'"
        print(f"✅ Test case {i+1} passed!")

if __name__ == "__main__":
    run_tests()