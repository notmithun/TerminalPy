#import keyboard
import random
import os
TerminalMainID = random.randint(1000, 999999)
os.system("clear")
print("ALERT! THIS TERMINAL ONLY SUPPORTS LINUX BASH COMMANDS! I'M TELLING THIS BECAUSE CLEAR IN WINDOWS CMD IS CLS SO, IF YOU PUT CLEAR IN CMD IT WILL JUST SAY ERROR!")

User = input("Name(Terminal Name): ")
R = True
PassMgr = False
os.system("clear")
print("Copyright MithunCreations 2023")
print(f"Id: {TerminalMainID}")
while R:
    TerminalMain = input(f"{User}$: ")
    if TerminalMain == "help" or TerminalMain == "Help":
        print("Version: 1.0.0")
        print("Version Name: FV")
        print("report.ver.file: To write the version detials on .log file")
        print("report.ver: To Print the version detials")
        print("print: to print something")
        print("exit.main: to end the session")
        print("root.enter: enter the root session")
        print("cls / clear: To clear / clean your terminal")
        print("read.file.lines: To read the lines of the file")
        print("read.file: to read the text in the file")
        print("speak.sound: It's a text to speach(tts)")
        print("That is all commands for this version")
    elif TerminalMain == "report.ver.file":
        filename = "Version.log"
        mode = "w"
        with open (filename, mode) as file:
            file.write("Version 1.1.1 \n")
            file.write("Version Name: FV \n")
            file.write("The First Version \n")
    elif TerminalMain == "report.ver":
        print("Version 1.0.0 \n")
        print("Version Name: FV \n")
        print("The First Version \n")
        print("Added Space (/n) in report.ver.file Update 1.0.1")
        print("Created the root! Update 1.1.1")
    elif TerminalMain == "print":
        TerminalPrint = input("Enter something: ")
        print(TerminalPrint)
    elif TerminalMain == "exit.main":
        print("Session Ended")
        R = False
        TerminalMain = input("Press any key to contiune")
        os.system("clear")
    elif TerminalMain == "root.enter":
        if PassMgr == True:
            TerminalMainPassword = input("Please Enter your password: ")
            if TerminalMainPassword == TerminalPassMgrMain:
                TerminalRootID = random.randint(999, 9999999)
                root = True
            else:
                print("Incorrect Password")
        elif not PassMgr == True:
            root = True
        while root:
            TerminalRoot = input(f"{User}@root#: ")
            if TerminalRoot == "user.account.name(change)":
                if PassMgr == True:
                    TerminalRootPassword = input("Please enter your password: ")
                    print("Correct \n")
                    print("Change your name \n")
                    TerminalRootCN = input("Re-enter the terminal name: ")
                    User = TerminalRootCN
                elif not PassMgr == True or PassMgr == False:
                    print("Change your name \n")
                    TerminalRootCN = input("Re-enter the terminal name: ")
                    User = TerminalRootCN
            elif TerminalRoot == "help.root" or TerminalRoot == "help":
                print("Root Logined")
                print("root.main.exit: to end the root session / get back to normal session")
                print("user.account.name(change): To change the main / termianl user name")
                print("user.account.password: To set a password to the user")
                print("user.account.password.false: To Delete the password")
                print("main.end: to end the main session")
            elif TerminalRoot == "root.main.exit":
                if PassMgr == True:
                    TerminalRootPassMgr = input("Please enter your password: ")
                    if TerminalRootPassMgr == TerminalPassMgrMain:
                        print("Password Correct! \n \n Session Ended")
                        root = False
                    else:
                        print("Wrong Password! \n")
                elif PassMgr == False:
                    print("Session Ended")
                    root = False
            elif TerminalRoot == "user.account.password":
                print("Welcome to the Password Set")
                PassMgr = True
                TerminalPassword = input("Enter the password: ")
                TerminalPassMgrMain = TerminalPassword
            elif TerminalRoot == "user.account.password.false":
                TerminalRootAlert = input("Are you sure you want to delete the password?: ")
                if TerminalRootAlert == "yes" or TerminalRootAlert == "y":
                    TerminalRootPassMgr = input("Please enter the password to contiune: ")
                    if TerminalRootPassMgr == TerminalPassMgrMain:
                        PassMgr = False
                        TerminalPassword = None
                    if not TerminalRootPassMgr == TerminalPassword:
                        print("Password incorrect!")
                        print("Failed to change the password")
                if TerminalRootAlert == "no" or TerminalRootAlert  == "n":
                    print("Password did not delete!")
            elif TerminalRoot == "main.end":
                if PassMgr == True:
                    TerminalRootPassword = input("Please enter your password: ")
                    if TerminalRootPassword == TerminalPassMgrMain:
                        print("The Main Session Ended")
                        root = False
                        R = False
                    else:
                        print("Incorrect Password")
                elif not PassMgr == True or PassMgr == False:
                    print("The Main Session Ended")
                    root = False
                    R = False
            elif  TerminalRoot == "root.change.system":
                print("X", "\n Failure!")
            elif TerminalRoot == "cls" or TerminalRoot == "clear":
                os.system("clear")
            elif TerminalRoot == "" or TerminalRoot == " ":
                pass
            elif TerminalRoot == "id.refer.print":
                print(f"Your ID is {TerminalRootID}")
            elif TerminalRoot == "id.reset":
                if PassMgr == True:
                    TerminalRootPassword = input("Enter the password")
                    if TerminalRootPassword == TerminalPassMgrMain:
                        TerminalRootID = random.randint(999, 9999999)
                    else:
                        print("Incorrect Password!")
                elif PassMgr == False or not PassMgr == True:
                    TerminalRootID = random.randint(999, 9999999)
            elif TerminalRoot == "id.set.mainuser.reset":
                if TerminalRootPassword == TerminalRootPassMgr:
                    print("ID Is Reseting...")
                    TerminalMainID = random.randint(999, 999999)
            else:
                print("Unknown Command!")
    elif TerminalMain == "read.file.lines":
        TerminalMainFileName = input("Enter the file name (Also please include the file extention example: .txt, .py, etc...): ")
        try:
            TerminalMainFile = open(TerminalMainFileName, "r")
            c = 0
            ct = TerminalMainFile.read()
            cl = ct.split("\n")
            for i in cl:
                if i:
                    c += 1
            print(f"Lines in the file are {c}")
        except FileNotFoundError:
            print("No Such File Found")

    elif TerminalMain == "" or TerminalMain == " ":
        pass
    elif TerminalMain == "cls" or TerminalMain == "Clean" or TerminalMain == "Clear" or TerminalMain == "Clr":
        os.system("clear")
    elif TerminalMain == "id.refer.print":
        print(f"Your ID: {TerminalMainID}")
    #elif keyboard.is_pressed("up"):
        #print("UP KEY NOT YET SUPPORTED IN LINUX AND WINDOWS!")
    elif TerminalMain == "speak.sound":
        print("Due to some problems this not working in linux", "\n \n But Windows is working")
    elif TerminalMain == "read.file":
        TerminalMainFileName = input("Enter the file name (Also please include the file extention example: .txt, .py, etc...): ")
        try:
            TerminalMainFile = open(TerminalMainFileName, "r")
            print(TerminalMainFile.read(), "\n")
            print("File Read")
            TerminalMainFile.close()
        except FileNotFoundError:
            print("No Such File Found")
    else:  
        print("Unknown Command!")