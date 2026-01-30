def solution(firstArray, secondArray):
    # Build a trie from first array
    trie = {}
    for num in firstArray:
        node = trie
        for char in str(num):
            if char not in node:
                node[char] = {}
            node = node[char]
    
    # Find longest matching prefix for each number in second array
    max_len = 0
    for num in secondArray:
        node = trie
        length = 0
        for char in str(num):
            if char in node:
                length += 1
                node = node[char]
            else:
                break
        max_len = max(max_len, length)
    
    # Also check the other direction (build trie from secondArray)
    trie2 = {}
    for num in secondArray:
        node = trie2
        for char in str(num):
            if char not in node:
                node[char] = {}
            node = node[char]
    
    for num in firstArray:
        node = trie2
        length = 0
        for char in str(num):
            if char in node:
                length += 1
                node = node[char]
            else:
                break
        max_len = max(max_len, length)
    
    return max_len
