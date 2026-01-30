def solution(firstArray, secondArray):
    # Store all prefixes from first array in a set
    prefixes = set()
    for num in firstArray:
        s = str(num)
        for i in range(1, len(s) + 1):
            prefixes.add(s[:i])
    
    # Find longest matching prefix from second array
    max_len = 0
    for num in secondArray:
        s = str(num)
        # Check from longest to shortest, stop when found
        for i in range(len(s), max_len, -1):
            if s[:i] in prefixes:
                max_len = i
                break
    
    return max_len
