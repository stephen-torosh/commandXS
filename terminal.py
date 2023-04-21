

# Welcome to FireTR

# FireTR - is terminal application, which was written with Python 3.10.2


# importing modules

# os for system management
# colorama for initilizating color text
# time only for one function :D


from os import system
import os
from colorama import init, Fore, Style
import time
import random
import pyqrcode
import webbrowser
from ftrconfig import *


working = True

# bcolors class for color text

working = True


class bcolors:
    HEADER = B_HEADER
    OKBLUE = B_OKBLUE
    OKCYAN = B_OKCYAN
    OKGREEN = B_OKGREEN
    WARNING = B_WARNING
    FAIL = B_FAIL
    ENDC = B_ENDC
    BOLD = B_BOLD
    UNDERLINE = B_UNDERLINE


# at start
if (os.path.isdir("extensions")):
    pass
else:
    os.mkdir("extensions")

# init extensions


listOfExts = []

for index in range(len(os.listdir("extensions"))):
    a = os.listdir("extensions")[index]

    removedLast3CharsFromA = a[:-3]

    listOfExts.append(removedLast3CharsFromA)

# functions

# commands for paths


def ls(path):

    if os.path.isdir(path):
        files = os.listdir(path)
        files.sort()
        for f in files:
            if (os.path.isfile(f)):
                print(f"{bcolors.FAIL}{f}{bcolors.ENDC}")
            elif (os.path.isdir(f)):
                print(f"{bcolors.OKBLUE}{f}{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}-> FTR: directory not found{bcolors.ENDC}")


def cd(path):
    try:
        os.chdir(path)
        print(
            f"{bcolors.OKGREEN}-> FTR: Current directory successfully defined{bcolors.ENDC}")
    except:
        print(f"{bcolors.FAIL}-> FTR: Current directory does not exists{bcolors.ENDC}")

# commands for directories


def mkdir(path):
    try:
        os.mkdir(path)
        print(
            f"{bcolors.OKGREEN}-> FTR: Directory '{path}' successfully created{bcolors.ENDC}")
    except FileExistsError as error:
        print(f"{bcolors.FAIL}-> FTR: failed to create directory{bcolors.ENDC}")


def rmdir(path):
    if os.path.isdir(path):
        if os.listdir(path) != []:
            print(f"{bcolors.FAIL}Sorry, but directory is not empty, use rmf and rmdir commands to delete files and directories{bcolors.ENDC}")
        else:
            if os.path.isdir(path):
                os.rmdir(path)
                print(

                    f"{bcolors.OKGREEN}-> FTR: Directory '{path}' successfully removed{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}-> FTR: directory not found{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}Sorry, but '{path}' is not a directory{bcolors.ENDC}")

# commands for files


def rmf(filePath):
    if os.path.isdir(filePath):
        print(f"{bcolors.FAIL}Sorry, but '{filePath}' is not a file{bcolors.ENDC}")
    else:
        try:
            os.remove(filePath)
            print(
                f"{bcolors.OKGREEN}-> FTR: File '{filePath}' successfully removed{bcolors.ENDC}")
        except FileExistsError as error:
            print(f"{bcolors.FAIL}-> FTR: file not found{bcolors.ENDC}")


def genpass(length: int = 0):
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-=+<>?/][{}"
    password = ""
    lengthRange = range(random.randint(8, 32))
    if (length > 0):
        if (length > 128):
            return print(f"{bcolors.FAIL}Sorry, but password length can not be more than 128{bcolors.ENDC}")
        lengthRange = range(length)
    for i in lengthRange:
        password = password + chars[random.randint(0, 72)]
    print(password)


def generateQrCode(url: str):
    if (len(url) > 64):
        return print(f"{bcolors.WARNING}Sorry, but the maximum URL length is 64{bcolors.ENDC}")
    clearScreen()
    text = pyqrcode.create(url)
    print(text.terminal(module_color="yellow", background="blue", quiet_zone=1))


def genpass(length: int = 0):
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-=+<>?/][{}"
    password = ""
    lengthRange = range(random.randint(8, 32))
    if (length > 0):
        if (length > 128):
            return print(f"{bcolors.FAIL}Sorry, but password length can not be more than 128{bcolors.ENDC}")
        lengthRange = range(length)
    for i in lengthRange:
        password = password + chars[random.randint(0, 72)]
    print(password)


def generateQrCode(url: str):
    if (len(url) > 64):
        return print(f"{bcolors.WARNING}Sorry, but the maximum URL length is 64{bcolors.ENDC}")
    clearScreen()
    text = pyqrcode.create(url)
    print(text.terminal(module_color='yellow', background='blue', quiet_zone=1))


def cat(path):
    print("\n")
    if os.path.isfile(path):
        with open(path) as f:
            contents = f.read()
            print(f"{bcolors.OKBLUE}{contents}{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}-> FTR: file not found{bcolors.ENDC}")

# other


def clearScreen():
    system("cls")


def openBrowser(url):
    webbrowser.open_new(url)


def runPython3(file):
    if os.path.isfile(file):
        exec(open(file).read())
    else:
        print(
            f"{bcolors.FAIL}sorry but there is no file with name: {file}{bcolors.ENDC}")


def createFile(filePath, textLine):
    with open(filePath, "w") as f:
        f.write(textLine)
    print(f"{bcolors.OKGREEN}-> FTR: File '{filePath}' successfully created{bcolors.ENDC}")


def openBrowser(url):
    webbrowser.open_new(url)


def runPython3(file):
    if os.path.isfile(file):
        exec(open(file).read())
    else:
        print(
            f"{bcolors.FAIL}sorry but there is no file with name: {file}{bcolors.ENDC}")


def listCommands():
    print(f"{bcolors.OKGREEN}Available commands:{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}ls <directory> - show all files in current directory{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}mkdir <directory> - create directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}rmdir <directory> - remove directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}cat <file name> - read file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}crf <file name> - create file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}version - current version of fireTR{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}rmf <file name> - remove file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}cd <directory> - set the desired current directory to work with it{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}restart - restart FireTR{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}stop - stop FireTR{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}genpass <length> - generate hard password{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}qrcode <url> - generate qrcode from url{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}py <file name> - run python 3 file{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}help - it`s to get help, and you type it now :D{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}web <url> - open webbrowser with url in terminal{bcolors.ENDC}")


def printTooManyParamsErr(command):
    print(f"{bcolors.FAIL}Sorry, but the command '{command}' does not accept so many parameters{bcolors.ENDC}")


def stop():
    global working
    working = False


# commands definer


def command(value):
    arguments = value.split()
    lenOfValueList = len(arguments)

    if (lenOfValueList > 0):
        match arguments[0]:
            case "ls":
                if (lenOfValueList == 1):
                    ls(".")
                if (lenOfValueList == 2):
                    ls(arguments[1])
                if (lenOfValueList > 2):
                    printTooManyParamsErr("ls")
            case "cd":
                if (lenOfValueList == 1):
                    cd(".")
                if (lenOfValueList == 2):
                    cd(arguments[1
                                 ])
                if (lenOfValueList > 2):
                    printTooManyParamsErr("cd")
            case "py":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of python file: py <name of file>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    runPython3(arguments[1])
                if (lenOfValueList > 2):
                    printTooManyParamsErr("py")
            case "mkdir":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of new directory: mkdir <name of dir>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    mkdir(arguments[1])
                if (lenOfValueList > 2):
                    printTooManyParamsErr("mkdir")
            case "rmdir":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of directory: rmdir <name of dir>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    rmdir(arguments[1])
                if (lenOfValueList > 2):
                    printTooManyParamsErr("rmdir")
            case "crf":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of new file: crf <name of file>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    createFile(arguments[1], "")
                if (lenOfValueList > 2):
                    printTooManyParamsErr("crf")
            case "web":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter url: web <url>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    openBrowser(arguments[1])
                if (lenOfValueList > 2):
                    printTooManyParamsErr("web")
            case "rmf":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of file: rmf <name of file>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    rmf(arguments[1])
                if (lenOfValueList > 2):
                    printTooManyParamsErr("rmf")
            case "cat":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of file: cat <name of file>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    cat(arguments[1])
                if (lenOfValueList > 2):
                    printTooManyParamsErr("cat")
            case "version":
                print("FTR: version: 1.2 official")
            case "help":
                listCommands()
            case "genpass":
                if (lenOfValueList == 1):
                    genpass()
                if (lenOfValueList == 2):
                    genpass(int(arguments[1]))
                if (lenOfValueList > 2):
                    printTooManyParamsErr("genpass")
            case "restart":
                time.sleep(1)
                os.chdir(".")
                start()
            case "qrcode":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of url: qrcode <url>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    generateQrCode(arguments[1])
                if (lenOfValueList > 2):
                    printTooManyParamsErr("qrcode")

            case "stop":
                if (lenOfValueList == 1):
                    stop()
                if (lenOfValueList > 1):
                    printTooManyParamsErr("stop")
            case _:
                firstIndex = arguments[0]
                print(f"unknown command: {firstIndex}")

    elif (lenOfValueList == 0):
        pass


# initilizating colorama
init()

# starting app


def start():
    os.chdir(".")
    print("FireTR 1.2 official\n")
    print("Copyright(c) FireInc corporation\n")
    print("Type 'help' to get help\n")


start()


while working:
    commandEnterred = input("FTR <" + os.getcwd() + "> #: ")

    command(commandEnterred)
