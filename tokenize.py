#import nltk
import os
import io
import re
#wordarray = []
#chatarray = []
#text1 = "Test:"


wordlist = input("What is your word list called?")
f = open(wordlist)
l = set(w.strip().lower() for w in f)
chatlog = input("What is your chat log called?")
with open(chatlog) as f:
    found = False
    for line in f:
        line = line.lower()
        if any(w in line for w in l):
            print (l)
            print(line)
            found = True
    if not found:
        print("not here")



    #    if not found:
        #    print("not here")


#wordlist = input("What is your word list file called?")
#with open(wordlist, 'r') as w:
#       wordlines = wordlist.readlines()
#       for line in wordlines:
#           print (line)

     #  chatlist = input("What is your chat log called?")
    #   with open(chatlist, 'r') as c:
        #    for line in c:
        #        chatlist = line.split()




#wordlist = input("What is your word list file called?")
#with open(wordlist, 'r') as w:
#    for line in w:
#        wordlist = line.split()
#        chatlist = input("What is your chat log called?")
#        with open(chatlist, 'r') as c:
#            for line in c:
#                chatlist = line.split()
#                for wordlist in chatlist:
#                    if wordlist == chatlist:
#                        print (chatlist)
#                        break





#    wordread = w.readlines()
#    chat = input("What is your chat log file called?")
#    with open(chat) as c:
#        chatread = c.readlines()
#        dictionary = set(line.strip() for line in chatread)
#        for line in chat:
#            word, freq=line.split()
#            if dictionary in chat:
#                    print (word)
#

#reader = input("what is your filename?")
#fh = open(reader, 'r')
#alllines = fh.readlines()
#print (alllines)
#fh.close()
