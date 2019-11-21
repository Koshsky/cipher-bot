#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import secret
import module, alphabet
import vk_api
import random
import caesar, vigenere, morse

vk = vk_api.VkApi(token=secret.TOKEN)

def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])
def send(text, id):
    """
    отправить сообщение
    """
    vk.method('messages.send',  {'peer_id' : id,'message' : text, 'random_id' : get_random_id()})
    
while True:
    messages = vk.method('messages.getConversations', {'offset': 0, 'count': 20, 'filter': 'unread'})
    if messages['count'] > 0:
        id = messages['items'][0]['last_message']['from_id']
        body = messages['items'][0]['last_message']['text']  # текст сообщения
        body = list(str(body.lower()).split()) 
        print(len(body), '\t', body)
        if len(body) != 0:
            if body[0] in module.caesar:
               if len(body) >  3:
                    try:
                       if body[1] in module.cipher:
                           send(caesar.cipher(str(body[3:]), int(body[2])), id)

                       elif body[1] in module.decipher:
                           send(caesar.decipher(str(body[3:]), int(body[2])), id)

                       else:
                           send(module.caesar_help, id)

                    except:
                        send(module.caesar_help, id)

               else:
                   send(module.caesar_help, id)

            elif body[0] in module.cipher:
                send(module.caesar_help, id)

            elif body[0] in module.vigenere:
                if len(body) >  3 and (alphabet.lang(body[2]) == 'rus' or alphabet.lang(body[2]) == 'eng'):
                    if body[1] in module.cipher:
                       send(vigenere.cipher(' '.join(body[3:]), body[2]), id)

                    elif body[1] in module.decipher:
                       send(vigenere.decipher(' '.join(body[3:]), body[2]), id)

                    else:
                       send(module.vigenere_help, id)

                else:
                    send(module.vigenere_help, id)


            elif body[0] in module.morse:
                if len(body) > 1:
                    send(morse.cipher(body[1:]), id)
                else:
                    send(module.morse_help, id)
            else:
               send(module.help_send, id)
