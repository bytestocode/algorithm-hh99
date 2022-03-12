import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = collections.defaultdict(list)
print(anagrams)

for word in strs:
    print(sorted(word))
    anagrams[''.join(sorted(word))].append(word)

print(anagrams)
print(anagrams.values())
print(list(anagrams.values()))


def fn(arr):
    return len(arr)


print(sorted(list(anagrams.values()), key=fn))
