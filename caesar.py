import alphabet

def cipher(string, KEY):
        string = str(''.join(string).lower())
        output = ''
        for i in string:
            if i.isalpha():
                if alphabet.lang(i) == 'rus':
                    letter = alphabet.rus[i] + KEY
                    if letter > 33:
                        output += chr(alphabet.rus[letter - 33])

                    else:
                        output += chr(alphabet.rus[letter])

                elif alphabet.lang(i) == 'eng':
                    letter = alphabet.eng[i] + KEY
                    if letter > 26:
                        output += chr(alphabet.eng[letter - 26])

                    else:
                        output += chr(alphabet.eng[letter])
            else:
                output += i
        return output.lower()

def decipher(string, KEY):
        string = str(''.join(string).lower())
        output = ''
        for i in string:
            if i.isalpha():
                if alphabet.lang(i) == 'rus':
                    letter = alphabet.rus[i] - KEY
                    if letter < 1:
                        output += chr(alphabet.rus[letter + 33])

                    else:
                        output += chr(alphabet.rus[letter])

                elif alphabet.lang(i) == 'eng':
                    letter = alphabet.eng[i] + KEY
                    if letter < 1:
                        output += chr(alphabet.eng[letter + 26])

                    else:
                        output += chr(alphabet.eng[letter])
            else:
                output += i
        return output.lower()

