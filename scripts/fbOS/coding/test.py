def groupShiftedStrings(strings):
    """
    Given an array of strings, group anagrams together.

    :type strings: List[str]
    :rtype: List[List[str]]
    """
    # Create a dictionary to store the anagrams
    anagrams = {}
    for string in strings:
        # Sort the string
        sorted_string = ''.join(sorted(string))
        # If the sorted string is already in the dictionary, add the string to the list
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        # Else, create a new key and add the string to the list
        else:
            anagrams[sorted_string] = [string]
    # Return the values of the dictionary
    return anagrams.values()