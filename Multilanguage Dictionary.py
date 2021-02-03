response = {
    "Langsel1" : "Enter your first language: \n", 
    "Langsel2" : "Now enter your second language: \n",
    "Help" : """To add a word/phrase to your dictionary, type add, to search for an existing word/phrase,
type search, to show all existing words/phrases, type list to show all current entries, to bring this message back up, type 'help'\n""",
    "Lang1" : "Enter your word/phrase\n",
    "Lang2" : "Enter the meaning of your word/phrase\n",
    "Added" : "Successfully added word!\n",
    "Search" : "Enter your word, phrase, or definition\n",
    "Error" : "Sorry, that didn't work\n",
    "Next" : "What would you like to do next\n",
    "Select" : "Which Language do you want to search by \n"
}

class Language:
    def __init__(self):
        self.langdict = {"hello" : "hej"}

    def add(self, key, definition):
        self.langdict[key] = definition
        if self.langdict[key]:
            print(response["Added"])
        else:
            print(response["Error"])

    def keysearch(self, search):
        if self.langdict[search]:
            print("Definition: " + self.langdict[search])
        else:
            print(response["Error"])

    def valsearch(self, search):              
            for key, value in self.langdict.items():
                if search == value:
                    print("Definition: " + key)

    def display(self):
        i=1
        for key,value in self.langdict.items():
            
            print(i + ". " + key + " | " + value + "\n")
            i+= 1

lang1 = input(response["Langsel1"])
lang2 = input(response["Langsel2"])
langdict = Language()
x = input(response["Help"])

while x != "exit":
    if x == "add":
        original = input(response["Lang1"])
        translation = input(response["Lang2"])
        langdict.add(original, translation)
    elif x == "search":
        a = input(response["Select"] + lang1 + " or " + lang2 + "?\n")
        word = input(response["Search"])
        if a == lang1:
            langdict.keysearch(word)
        elif a == lang2:
            langdict.valsearch(word)
        else:
            print(response["Error"])
    elif x == "list":
        langdict.display()
    elif x == "help":
        print(response["Help"])
    else:    
        print(response["Error"])
    x = input(response["Next"])



# Alright, build a command line application that acts as a bilingual dictionary. 
# Users can select a first language and a second language. They can enter a word or phrase for either the first 
# or second language and then a definition of the word or phrase. Users should also be able to 
# look up existing phrases either by the phrase itself, by its definition, or just by listing them all