import alphabet

def cipher(a):
    string_array = [i.split() for i in a]
    output = ''
    for i in string_array:
        for j in i:
            if j in alphabet.morse:
                output += alphabet.morse[j]
        output += ' '
    return output
