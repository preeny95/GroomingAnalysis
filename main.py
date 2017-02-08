import nltk
import os
import io

#Function that gets the file name for a words list and places into an array
def __file__(wordsfile):
    reader = input("what is your filename?")
    if os.path.exists(reader) == True:
        r = (reader)
        with open(reader, 'r') as tdata:
            content = tdata.read()
#Function that allows a user to add thier own key words to a file.
def __nosavefile__():
        addword = []
        i=0
        while 1:
            i+=1
            addword_array=input("Enter your words (Press enter when finished): ")
            addword.append(addword_array)
            if addword_array=='':
                addword.remove('')
                print (addword)
                break
#Allows the user to create a word list file and adds all the words from the array
#into that file for analysis
def __savefile__():
    savename=input("Enter the name of your file:")
    addword = []
    i=0
    while 1:
        addword_array=input("Enter your words (Press enter when finished): ")
        addword.append(addword_array)
        with io.open(savename, 'w') as f:
            f.writelines(line + u'\n' for line in addword)
        with open(savename, 'r') as f:
            addword = [line.rstrip(u'\n') for line in f]
        if addword_array=='':
            addword.remove('')
            print (addword)
            break

#Function that gives the user the option to save the word list to a file.
def __savefilequestion__():
    savefilequestion=input("Would you like to save your wordlist to a file?")
    if savefilequestion in ['y', 'Y', 'Yes', 'YES']:
        __savefile__()
    elif savefilequestion in ['n', 'N', 'No', 'NO']:
            __nosavefile__()
#Function that asks the user if they would like to create a word list
#or import a already created list
wordsfile = str(input("Would you like to create a word list?"))
if wordsfile in ['y', 'Y', 'Yes', 'YES']:
    __savefilequestion__()
elif wordsfile in ['n', 'N', 'No', 'NO']:
    __file__(wordsfile)
