'''
Welcome to FireTR

FireTR - is terminal application, which was written with Python 3
'''


# importing modules

# os for system management
# colorama for initilizating color text
# time only for one function :D


from os import system
import os
from colorama import init, Fore, Style
import time

# bcolors class for color text


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# functions

# commands for paths


def ls(path):
    if os.path.isdir(path):
        files = os.listdir(path)
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


def createFile(filePath, textLine):
    with open(filePath, 'w') as f:
        f.write(textLine)
    print(f"{bcolors.OKGREEN}-> FTR: File '{filePath}' successfully created{bcolors.ENDC}")


def cat(path):
    if os.path.isfile(path):
        with open(path) as f:
            contents = f.read()
            print(contents)
    else:
        print(f"{bcolors.FAIL}-> FTR: file not found{bcolors.ENDC}")

# other


def clearScreen():
    system('cls')


def listCommands():
    print(f"{bcolors.OKGREEN}Available commands:{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}ls - show all files in current directory{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}mkdir - create directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}rmdir - remove directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}cat - read file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}crf - create file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}version - current version of fireTR{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}rmf - remove file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}cd - set the desired current directory to work with it{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}restart - restart FireTR{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}help - it`s to get help, and you type it :D{bcolors.ENDC}")

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
            case "cd":
                if (lenOfValueList == 1):
                    cd(".")
                if (lenOfValueList == 2):
                    cd(arguments[1])
            case "mkdir":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of new directory: mkdir <name of dir>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    mkdir(arguments[1])
            case "rmdir":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of directory: rmdir <name of dir>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    rmdir(arguments[1])
            case "crf":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of new file: crf <name of file>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    createFile(arguments[1], "")
            case "rmf":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of file: rmf <name of file>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    rmf(arguments[1])
            case "cat":
                if (lenOfValueList == 1):
                    print(
                        f"{bcolors.FAIL}Please, enter name of file: cat <name of file>{bcolors.ENDC}")
                if (lenOfValueList == 2):
                    cat(arguments[1])
            case "version":
                print("FTR: version: 1.2 official")
            case "help":
                listCommands()
            case "restart":
                time.sleep(1)
                os.chdir(".")
                start()
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
    print("Copyright (c) FireInc corporation\n")
    print("Type 'help' to get help\n")


start()

while True:
    commandEnterred = input("FTR <" + os.getcwd() + "> #: ")

    command(commandEnterred)
