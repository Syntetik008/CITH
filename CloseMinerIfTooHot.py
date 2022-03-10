import os
import GPUtil
import time

def clear():
    print(" \n" * 80)

def gpuCheck():
    clear()
    print("What process do you want to close? e.g Notepad.exe")
    print(" ")
    processN = input(">> ")
    clear()
    print("At what temperature u want to close it? use xx.0 e.g 61.0")
    print(" ")
    processT = input(">> ")
    processT2 = float(processT)
    loopnum = 0
    while loopnum < 1:
        gput = GPUtil.getGPUs()[0]
        print("GPU temp: ", gput.temperature, "c")
        if gput.temperature > processT2:
            os.system("TASKKILL /F /IM " + processN)
            while loopnum < 1:
                gput = GPUtil.getGPUs()[0]
                print("GPU temp: ", gput.temperature, "c // Process " + processN + " has been closed")
                time.sleep(1)
        time.sleep(1)


def cpuCheck():
    print("//TODO")

def bothCheck():
    print("//TODO")

def mainMenu():
    print("Welcome to CITH")
    print("Choose what temperature u want to check")
    print(" ")
    print("[1] GPU")
    print("[2] CPU //TODO")
    print("[3] Both //TODO")
    print(" ")
    print("WARNING: might not work on other than nvidia gpus ")
    CheckT = input(">> ")
    if CheckT == "1":
        gpuCheck()
    elif CheckT == "2":
        #cpuCheck()
        mainMenu()
    elif CheckT == "3":
        #bothCheck()
        mainMenu()
    else:
        mainMenu()

mainMenu()