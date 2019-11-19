def lang(KEY):
    """
    алфавит
    """
    for i in KEY:
        if not i.isalpha():
            return ''
            break
    else:
        KEY_LANG = 'mix'
        if 'a' <= KEY[0].lower() <= 'z':
            for i in KEY:
                if not ('a' <= i <= 'z'):
                    break
            else:
                KEY_LANG = 'eng'  # english
                
        elif 'а' <= KEY[0].lower() <= 'я':
            KEY = KEY.replace('ё', '')
            for i in KEY:
                if not ('а' <= i <= 'я'):
                    break
            else:
                KEY_LANG = 'rus' # russian
                
        elif '0' <= KEY[0].lower() <= '9':
            for i in KEY:
                if not ('0' <= i <= '1'):
                    break
            else:
                KEY_LANG = 'num' # number
        return KEY_LANG

def cipher(string, KEY):
    """
    Шифровка слова
    """
    KEY = KEY.replace('ё', 'е').lower()
    output = ''
    list_of_keys = []
    string = str(''.join(string).lower())
    
    if lang(KEY) == 'rus':
        for i in KEY:
            list_of_keys.append(int(ord(i) - 1071))
    elif lang(KEY) == 'eng':
        for i in KEY:
            list_of_keys.append(int(ord(i) - 96))
            
    count = 0
    i = 0
    
    while i != len(string):
        if count < len(list_of_keys):
            if string[i].isalpha():
                letter = ord(string[i].lower()) + list_of_keys[count]
                if lang(KEY) == 'rus':
                    max_letter_ord = 1072
                    len_lang = 32
                elif lang(KEY) == 'eng':
                    max_letter_ord = 122
                    len_lang = 26
                while letter > max_letter_ord:
                    letter -= len_lang
                output += chr(letter)
            else:
                output += string[i]
            count += 1
            i += 1
        else:
            count = 0
    return 'Зашифрованный текст: ' + output.lower()

def decipher(string, KEY):
    """
    Расшифровка слова
    """
    KEY = KEY.replace('ё', 'е').lower()
    output = ''
    list_of_keys = []
    string = str(''.join(string).lower())
    
    if lang(KEY) == 'rus':
        for i in KEY:
            list_of_keys.append(int(ord(i) - 1071))
    elif lang(KEY) == 'eng':
        for i in KEY:
            list_of_keys.append(int(ord(i) - 96))
            
    count = 0
    i = 0
    
    while i != len(string):
        if count < len(list_of_keys):
            if string[i].isalpha():
                letter = ord(string[i]) - list_of_keys[count]
                
                if lang(KEY) == 'rus':
                    max_letter_ord = 1072
                    len_lang = 32
                    
                elif lang(KEY) == 'eng':
                    max_letter_ord = 122
                    len_lang = 26
                    
                while letter < max_letter_ord:
                    letter += len_lang
                    
                output += chr(letter)
            else:
                output += string[i]
            count += 1
            i += 1
        else:
            count = 0
    return 'Дешифрованный текст: ' + output.lower()
