#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import secret
import rendom
import caeser

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
        body = list(messages['items'][0]['last_message']['text'].lower())
 """
помощь
"""
        if body[0] in module.help:
            if len(body) > 1:
            
                if body[1] in module.cipher:
                    send(module.cipher_help, id)
                    
                elif body[1] in module.caeser:
                    send(module.ceaser_help, id)
                    
                elif body[1] in module.vigenere:
                    send(module.vigenere_help, id)
                    
                else:
                    send(module.help_send, id)
                    
            else:
                send(module.help_send, id)
"""
самый сок
"""
"""
caeser
       """
       elif body[0] in module.caeser:
          if len(body) >  3:
          
              if body[1] in module.cipher:
                  send(caeser.cipher(body[3:], body[2]), id)
                  
              elif body[1] in caeser.decipher:
                  send(caeser.decipher(body[3:], body[2]), id)
                  
              else:
                  send(module.caeser_help, id)
                  
          else:
              send(module.caeser_help, id)
"""
vigenere
"""
       else:
          send('че', id)
                
