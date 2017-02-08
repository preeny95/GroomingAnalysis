#import nltk
import os
import io
import difflib

#wordarray = []
#chatarray = []
#text1 = "Test:"

wordlist = input("What is your word list file called?")
chatlog = input("What is your chat log called?")

f1 = open(wordlist)
f2 = open(chatlog)

f1_line = f1.readline()
f2_line = f2.readline()

line_no = 1

        # If a line does not exist on file2 then mark the output with + sign
if f2_line == '' and f1_line != '':
        print(">+", "Line-%d" % line_no, f1_line)
        # otherwise output the line on file1 and mark it with > sign
elif f1_line != '':
        print(">", "Line-%d" % line_no, f1_line)

        # If a line does not exist on file1 then mark the output with + sign
if f1_line == '' and f2_line != '':
        print("<+", "Line-%d" % line_no, f2_line)
        # otherwise output the line on file2 and mark it with < sign
elif f2_line != '':
        print("<", "Line-%d" %  line_no, f2_line)
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
