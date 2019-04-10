#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # kind of self explanatory
    if pattern in text:
        return True
    else:
        return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    indices = find_all_indexes(text, pattern)
    if len(indices) > 0:
        return indices[0]
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # wow much empty very string
    if pattern == '':
        return [position for position, character in enumerate(text)]

    # So what we're doing here is we are going through the source text exactly once.
    # for each character in the source text, we check if that character is the same
    # as the one that begins the search pattern. If so, we add its index to a hash table
    # of candidates, with the number of matching letters found so far as a value (1).
    # Then we go through the keys in the hash table. Conveniently, the number of matching letters
    # found so far is the same as the index of the next character in the pattern we need to match.
    # So we see if the current character in the text matches this. If so, we increase the value by 1.
    # If not, we change to value to False so we can ignore it for the rest of the loop.
    # If the key's value reaches the length of the pattern, then we know we have found a match,
    # so we append the key to our array of indices (because the key is the index of the first 
    # letter in the match) and set the value in the hash table to False since we're done with it.
    # time complexity - best case O(n), worse case O(mn)?
    # space complexity - best case O(1), worst case O(n)?
    indices = []
    candidates = {}
    delta = len(pattern)
    for position, character in enumerate(text):
        if character == pattern[0]:
            candidates[position] = 1
        for key, value in candidates.items():
            if value != False:
                if key != position and character == pattern[value]:
                    candidates[key] += 1
                elif key != position and character != pattern[value]:
                    candidates[key] = False
                if candidates[key] == delta:
                        indices.append(key)
                        candidates[key] = False
    return indices

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
