import alphabet

def cipher(string, KEY):
    """
    Шифровка слова
    """
    KEY = KEY.lower()
    output = ''
    list_of_keys = []
    string = str(''.join(string).lower())

    if alphabet.lang(KEY) == 'rus':
        for i in KEY:
            list_of_keys.append(alphabet.rus[i])
    elif alphabet.lang(KEY) == 'eng':
        for i in KEY:
            list_of_keys.append(alphabet.eng[i])
            
    count = 0
    i = 0
    
    while i != len(string):
        if count < len(list_of_keys):
            if string[i].isalpha():
                if alphabet.lang(string[i]) == 'rus':
                    letter = list_of_keys[count] + alphabet.rus[string[i]]
                    if letter > 33:
                        output += chr(alphabet.rus[letter - 33])
                        
                    else:
                        output += chr(alphabet.rus[letter])
                    
                elif alphabet.lang(string[i]) == 'eng':
                    letter = list_of_keys[count] + alphabet.eng[string[i]]
                    if letter > 26:
                        output += chr(alphabet.eng[letter - 26])
                    else:
                        output += chr(alphabet.eng[letter])
                count += 1
            else:
                output += string[i]
                
            i += 1
        else:
            count = 0
            
    return output.lower()

def decipher(string, KEY):
    """
    деШифровка слова
    """
    KEY = KEY.lower()
    output = ''
    list_of_keys = []
    string = str(''.join(string).lower())

    if alphabet.lang(KEY) == 'rus':
        for i in KEY:
            list_of_keys.append(alphabet.rus[i])
    elif alphabet.lang(KEY) == 'eng':
        for i in KEY:
            list_of_keys.append(alphabet.eng[i])
            
    count = 0
    i = 0
    
    while i != len(string):
        if count < len(list_of_keys):
            if string[i].isalpha():
                if alphabet.lang(string[i]) == 'rus':
                    letter = alphabet.rus[string[i]] - list_of_keys[count]
                    if letter < 1:
                        output += chr(alphabet.rus[letter + 33])
                        
                    else:
                        output += chr(alphabet.rus[letter])
                    
                elif alphabet.lang(string[i]) == 'eng':
                    letter = alphabet.eng[string[i]] - list_of_keys[count]
                    if letter < 1:
                        output += chr(alphabet.eng[letter + 26])
                    else:
                        output += chr(alphabet.eng[letter])
                count += 1
            else:
                output += string[i]
                
            i += 1
        else:
            count = 0
            
    return output.lower()

