s = "race a car"
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # regular expression
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]
        
