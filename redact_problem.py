#!python

from set import Set

# Time complexity: O(n+m) = O(n)
# Space complexity: ~O(n)?; best case O(m), worst case O(n+m)
# def redact_words(words, banned_words):
#     redacted = []
#     naughtySet = Set(banned_words)

#     for word in words:
#         if word not in naughtySet:
#             redacted.append(word)

#     return redacted

def redact_words(words, banned_words):
    naughtySet = Set(banned_words)

    return filter(lambda word: word not in naughtySet, words)
