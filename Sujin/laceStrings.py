def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here

    output = ''
    for i in range(len(s1)):
        for i in range(len(s2)):
            output += s1[i:i+1]+s2[i:i+1]
        return output+s1[i+1:]
    if len(output) == 0:
        return ''    
               