from os import system, name

# define our clear function
def clear(): # from Geeks For Geeks website
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def repeat(callback, arg = "!\\!"):
    again = "y"
    while again == "y":
        clear()
        if arg ==  "!\\!": #if there no argument
            callback()
        else:
            callback(arg)
        again = ""
        while again != "y" and again != "n":
            again = input("Try again? type [Yy/Nn] for yes/no: ").lower()