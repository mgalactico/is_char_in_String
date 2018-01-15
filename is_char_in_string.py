def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    # if string is empty, we did not find the char
    if len(aStr) == 0:
        return False
    else:
        middle = int(len(aStr) / 2)

    # if string is of length, check if ti matches char
    if len(aStr) == 1:
        return aStr == char

    # if the char is in the middle, check if there is a match
    if char == aStr[middle]:
        return True
    # recursively search on second half of the string
    elif char > aStr[middle]:
        aStr = aStr[middle+1:]
        return isIn(char, aStr)
    # recursively search on first half of the string
    elif char < aStr[middle]:
        aStr = aStr[:middle]
        return isIn(char, aStr)

print(isIn('a', ''))
print(isIn('x', 'djjlmnppruyz'))
print(isIn('k', 'bccgiosv'))
print(isIn('y', 'defgjjlmnnortvvvwwwz'))
print(isIn('y', 'defgjjlmnnortvvvwwwz'))
print(isIn('d', 'abcdefg'))
print(isIn('e', 'abcdefg'))
print(isIn('b', 'abcdefg'))
print(isIn('d', 'd'))
print(isIn('d', 'b'))
print(isIn('b', 'd'))
print(isIn('z', 'abcdefg'))
print(isIn('d', 'e'))
print(isIn('d', ' '))
