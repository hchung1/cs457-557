def conversion (text, string):
    textn=""
    stringi=string[::-1]
    for i in range(len(text)):
        j=string.find(text[i])
        if text[i] == string[j]:
            textn+=stringi[j]
        if text[i] != string[j]:
            textn+=text[i]

    return textn
