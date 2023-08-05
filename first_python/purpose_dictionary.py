import json
from myModule import repeat
import os

FILE = 'purpose_dictionary.json'


def sarch():
    f = open(FILE, "r")
    j = json.load(f)

    key1 = input("Enter the first leter in the word to sarch: ").lower() # lower() use to decrease mismatch example: atom and Atom

    if key1 in j:
        for word in j[key1]:
            print(word)
        key2 = input("Choos the word to get the definition: ").lower()
        if key2 in j[key1]:
            print(j[key1][key2])
        else:
            print("No word like this")
    else:
        print("No words for this litter")

    f.close()
    

def addOrEditWord():
    f = open(FILE, "r")
    j = json.load(f)
    f.close()
    
    f = open(FILE, "w")

    word = input("Enter the word: ").lower().replace(" ","") # .replace(" ","") use to decrease mismatch example: 'atom' and 'atom '
    description = input("Enter the description: ")
    letter = word[0].lower()
    letterList = {}
    if letter in j:
        letterList = j[letter]
    j[letter] = letterList
    j[letter][word] = description

    f.write(str(j).replace("\'","\"")) # json format writen by "" not ''

    f.close()

def delete():
    f = open(FILE, "r")
    j = json.load(f)
    f.close()
    
    f = open(FILE, "w")

    word = input("Enter the word: ").lower().replace(" ","")
    letter = word[0].lower()
    if letter in j:
        if word in j[letter]:
            j[letter].pop(word)
            if len(j[letter]) == 0:
               j.pop(letter)
            print("deleted")
        else:
            print("word not found")
    else:
        print("word not found")


    f.write(str(j).replace("\'","\""))

    f.close()


def dictionary():
    while True:
        choice = input("[Ss/Ee/Dd] sarch/add or edit word/delete: ").lower()
        if choice == "s":
            sarch()
            break
        elif choice == "e":
            addOrEditWord()
            break
        elif choice == "d":
            delete()


try:
    if os.stat(FILE).st_size == 0: # if the file empty
            f = open(FILE, "w")
            f.write("{}")
            f.close()
    repeat(dictionary)
except:
    print("Go to correct directory (type) ==> cd first_python")
    exit 

