def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if lengths are different
    if len(str1) != len(str2):
        return False
    
    # Create frequency dictionaries for both strings
    freq1 = {}
    freq2 = {}
    
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
    
    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
    
   
