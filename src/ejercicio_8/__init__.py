def check_anagram(word1, word2):
    inverso = word2[::-1]
    return "Son anagramas" if word1 == inverso else "No son anagramas"