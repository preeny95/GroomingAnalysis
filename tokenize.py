#import nltk
import os
import io
import difflib

#wordarray = []
#chatarray = []
#text1 = "Test:"

with open('words.txt') as fp:
    for line in fp:
        content = fp.readlines()
        content = [x.strip () for x in content]
        with open ('chat.txt') as fd:
            for line in fd:
                content1 = fd.readlines()
                content1 = [x.strip() for x in content1]
diffInstance = difflib.Differ()
diffList = list(diffInstance.compare(content1, content))

print ("Lines different in text1 from text2:")
for line in diffList:
  if line[0] == '-':
    print (line)
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
