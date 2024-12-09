
def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    lenght = len(s)
    hash_map = {}
    substr = ""

    for r in range(lenght):
        if s[r] in list(substr):
            hash_map[substr] = len(substr)
            l +=1
            substr = s[l:r+1]
        else:
            substr += s[r]

    hash_map[substr] = len(substr)

    print(hash_map)
        


        



s = "dvdf"

lengthOfLongestSubstring(s)