import numpy as np
import random
import string
import nltk
from nltk.chat.util import Chat, reflections


patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'hi|greeting|whats up|hey', ['Hey', 'hello', 'I am glad! You are talking to me']),
    (r'how are you?', ['I am doing well, thank you!, how are you?', 'I am fine, thanks!, how are you']),
    (r'I am fine|good', ['Great']),
    (r'what is your name?', ['My name is ChatBot.', 'You can call me ChatBot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
     ]
chatbot = Chat(patterns, reflections)



flag = True
print("BOT: My name is ChatBot. Let's hava a conversation! Also, if you want to exit any time, just type Bye!")
while(flag == True):
     user_input = input("You: ")
     if user_input.lower() == 'bye':
        break
     response = chatbot.respond(user_input)
     print("Chatbot:", response)
   
