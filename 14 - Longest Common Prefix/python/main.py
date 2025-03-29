def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = strs[0]

    for i in range(1, len(strs)):
        while strs[i][:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
    return prefix