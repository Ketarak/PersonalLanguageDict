dict1, dict2 = {},{}
response = [
    "Enter your first language",
    "Great! Now enter your second language: \n",
    """To add a word/phrase to your dictionary, type your language and .add, to search for an existing word/phrase,
    type search, to show all existing words/phrases, type list, to bring this message back up, type 'help'\n""",
    "Would you like to use your",
    "Successfully added word!",
    "Sorry there is no dictionary in \n",
    "Enter your word, phrase, or definition\n",
    "There is no dictionary with that name",
]
lang1= input(response[0])
lang2= input(response[1])
x = input(response[2])

class addWord:
    def __init__(self, l1): 
        self.first = l1

def addWord(language):
    word = input("enter the word for your " + language + " dictionary.\n")
    desc = input("enter the definition of your word\n")
    if language == lang1:
        dict1[word] = desc
        print("Successfully added word!")
    elif language == lang2:
        dict2[word] = desc
        print("Successfully added word!")
    else:
        print("Sorry there is no dictionary in \n" + language)
        return

def searchWord():
    search = input("Enter your word, phrase, or definition\n")
    if search in dict1 or dict1[search]:
        print("Word/Phrase: " + search)
        print("definition: " + str(dict1[search]))
    elif search in dict2 or str(dict2[search]):
        print("Word/Phrase: " + search)
        print("definition: " + str(dict2[search]))
    else:
        print("There is no dictionary with that name")
        return

def dictFull():
    while True:
        print("Show " + lang1 + " or " +lang2 + "?" + " type 'back' to go back to the menu\n")
        if input() == lang1:
            print(dict1)
            return
        elif input() == lang2:
            print(dict2)
            return
        elif input() == "back":
            return
        else:
            print("sorry this is not an option")

while True:
    if x == "add":
        language = input("Do you want to add a word in " + lang1 + " or " + lang2 + ("? \n"))
        addWord(language)
    elif x == "search":
        searchWord()
    elif x == "list":
        dictFull()
    elif x == "end":
        break
    else:
        print("sorry this is not an option\n")
    x = input()



#Alright, build a command line application that acts as a bilingual dictionary. Users can select a first language and a second language. They can enter a word or phrase for either the first 
#or second language and then a definition of the word or phrase. Users should also be able to look up existing phrases either by the phrase itself, by its definition, or just by listing them all