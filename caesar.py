def cipher(string, KEY):
        output = ''
        for i in string:
            if i.isalpha():
                letter = ord(i) + KEY
                if 'а' <= i.lower() <= 'я':
                    lower = 1072 <= letter <= 1103
                    upper = 1040 <= letter <= 1071
                    len_lang = 32
                elif 'a' <= i.lower() <= 'z':
                    lower = 97 <= letter <= 122
                    upper = 65 <= letter <= 90
                    len_lang = 26
                while not(upper or lower):
                    letter -= len_lang
                    if 'а' <= i.lower() <= 'я':
                        lower = 1072 <= letter <= 1103
                        upper = 1040 <= letter <= 1071
                    elif 'a' <= i.lower() <= 'z':
                        lower = 97 <= letter <= 122
                        upper = 65 <= letter <= 90
                output += chr(letter)
            else:
                output += i
        return 'Зашифрованный текст: ' + output.lower()

def decipher(string, KEY):
    output = ''
    for i in string:
        if i.isalpha():
            letter = ord(i) - KEY
            if 'а' <= i.lower() <= 'я':
                lower = 1072 <= letter <= 1103
                upper = 1040 <= letter <= 1071
                len_lang = 32
            elif 'a' <= i.lower() <= 'z':
                lower = 97 <= letter <= 122
                upper = 65 <= letter <= 90
                len_lang = 26
            while not(upper or lower):
                letter += len_lang
                if 'а' <= i.lower() <= 'я':
                    lower = 1072 <= letter <= 1103
                    upper = 1040 <= letter <= 1071
                elif 'a' <= i.lower() <= 'z':
                    lower = 97 <= letter <= 122
                    upper = 65 <= letter <= 90
            output += chr(letter)
        else:
            output += i
    return 'Дешифрованный текст: ' + output.lower()

