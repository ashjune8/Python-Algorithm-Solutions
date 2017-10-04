def findWords(words):
    wordlist = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    position = 0
    found = []

    while position < len(words):

        if (set(list(words[position].lower())) & set(list(wordlist[0].lower()))) == set(list(words[position].lower())):
            found.append(words[position])
        if (set(list(words[position].lower())) & set(list(wordlist[1].lower()))) == set(list(words[position].lower())):
            found.append(words[position])
        if (set(list(words[position].lower())) & set(list(wordlist[2].lower()))) == set(list(words[position].lower())):
            found.append(words[position])

        position += 1

    return found


print findWords(["Hello", "Alaska", "Dad", "Peace"])
