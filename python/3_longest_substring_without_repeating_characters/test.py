def test(s):
    l,r = 0,1
    lenght = len(s)
    hash_map = {}
    substr = ""

    while r != lenght + 1:
        if s[r-1] in list(substr):
            hash_map[substr] = len(substr)
            l +=1
            r = l + 1
            substr = s[l:r]
            r +=1
        else:
            substr = s[l:r]
            r += 1

    hash_map[substr] = len(substr)

    #print(max(hash_map.values()))
    print(hash_map)


test_cases = ["pwwkew", "nfpdmpi", "dvdf"]

for i in test_cases:
    test(i)