"""
LeetCode 1768: Merge Strings Alternately

Given two strings, merge them by alternating characters starting with word1.
If one string is longer, append the rest at the end.

Examples:
Input: word1 = "abc", word2 = "pqr"     → Output: "apbqcr"
Input: word1 = "ab", word2 = "pqrs"     → Output: "apbqrs"
"""

"""
Thought process

1. We need a variable that will hold the new string that is merged from word1 and word2 respectively

2. We need a way to compare whether word1 or word2 is longer or shorter than each other (len of each str and then use a comparison operator)

3. We need to loop through the shorter string to ensure we are not looping through uneccesary iterations as we can append the rest after our loop through the shorter str

4. Add word1 onto tracking variable then word2 respectively. Desctructering the correct letter is based on the loop iteration we are on and using the bracket notation.

5. Should there be be letters left in the longer str we can add onto the tracking variable using the length of the shorter str as the start and the length of the longer str as the end of the string extraction

6. Return the tracking variabe as final output
"""

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
        print(tracking)
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