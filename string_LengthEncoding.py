def stringCompressor(word):
    compressed_word = ""
    count_letter = ""
    count = 0
    
    for letter in word:
        if letter == count_letter:
            count += 1
        else:
            if count > 0:
                compressed_word += count_letter + str(count)
            count_letter = letter
            count = 1
    compressed_word += count_letter + str(count)
    
    if len(compressed_word) < len(word):
        return compressed_word
    else:
        return word


word='aaaabbbbaaac'
print(stringCompressor(word))