#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import secret
import module
import vk_api
import random
import caesar, vigenere

vk = vk_api.VkApi(token=secret.TOKEN)

def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])
def send(text, id):
    """
    отправить сообщение
    """
    vk.method('messages.send',  {'peer_id' : id,'message' : text, 'random_id' : get_random_id()})
    
while True:
    try:
        messages = vk.method('messages.getConversations', {'offset': 0, 'count': 20, 'filter': 'unread'})
        if messages['count'] > 0:
            id = messages['items'][0]['last_message']['from_id']
            body = list(messages['items'][0]['last_message']['text'].lower().split())

            if body[0] in module.help_info:
               send(module.help_send, id)

            elif body[0] in module.caesar:
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
                if len(body) >  3 and (vigenere.lang(body[2]) != 'num' and vigenere.lang(body[2]) != 'mix'):
                    if body[1] in module.cipher:
                       send(vigenere.cipher(' '.join(body[3:]), body[2]), id)

                    elif body[1] in module.decipher:
                       send(vigenere.decipher(' '.join(body[3:]), body[2]), id)

                    else:
                       send(module.vigenere_help, id)
                else:
                    send(module.vigenere_help, id)


            else:
               send(module.help_send, id)
    except:
        send('chocolates...', 475037544)
