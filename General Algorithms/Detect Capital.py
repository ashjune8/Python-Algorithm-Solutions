def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """

    if len(word) == 1:
        return True
    test = word.lower()
    i = 1;

    if word[0] == test[0]: #First Letter is Small
        while i < len(word):
            if word[i] != test[i]:
                return False

            i += 1
        return True
    elif word[1] != test[1]: #First Letter Capital and Second Letter also capital so all letters have to be capital
        i = 2
        while i < len(word):
            if word[i] == test[i]:
                return False

            i += 1
        return True
    else: #Only First Letter is Capital rest have to be small
        i =1
        while i < len(word):
            if word[i] != test[i]:
                return False

            i += 1
        return True





print detectCapitalUse('mL')

