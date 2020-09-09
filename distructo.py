import webbrowser as wb

import random

import tkinter

from tkinter import *

import subprocess

import os

import pyautogui, time

tk = Tk()

filecount = 1

wbcount = 1

btnclick = 1

memes = ["http://crossdivisions.com/"
    , "https://www.youtube.com/results?search_query=despacito"
         ,"https://Corndog.io",
"http://weirdorconfusing.com",
"http://Corndog.io",
"http://endless.horse/",
"http://burymewithmymoney.com/",
"http://quickdraw.withgoogle.com/#",
"http://movenowthinklater.com/"
,"http://www.google.com/search?riz=1C1CHBF_en-GBGB834GB834&biw=1327&bih3636&tbm=isch&sa3D1&ei=PTfkXMmJCpCmUNOXj7gK&q=9/11+cod&c"
,"http://beesbeesbees.com/",
"http://cat-bounce.com/",
"http://www.koalastothemax.com/","http://crossdivisions.com/"
    , "https://www.youtube.com/results?search_query=despacito"
         ,"https://Corndog.io",
"http://weirdorconfusing.com",
"http://Corndog.io",
"http://endless.horse/",
"http://burymewithmymoney.com/",
"http://quickdraw.withgoogle.com/",
"http://movenowthinklater.com/"
,"http://www.google.com/search?riz=1C1CHBF_en-GBGB834GB834&biw=1327&bih3636&tbm=isch&sa3D1&ei=PTfkXMmJCpCmUNOXj7gK&q=9/11+cod&c"
,"http://beesbeesbees.com/",
"http://cat-bounce.com/",
"http://www.koalastothemax.com/","http://cat-bounce.com/",
"http://www.koalastothemax.com/"]

def tkint():

    TK = Tk()


def Delete_file():

    try:
        os.remove("N://")

    except:

        Btn = Button()

        Btn.pack()

        Btn["text"]="Can't delete"



def MEMEZ():

    global wbcount

    wbcount = wbcount + 1

    site = random.randint(0,26)

    wb.open(memes[site])

    try:
        global filecount
        file = open("D:\\MemeSirLot().txt".format(filecount), "w+")
        file.write("According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground.")
        file.close()
        filecount = filecount + 1


    except:

        btn = Button()

        btn.pack()

        btn["text"]="No more storage, would you like to delet files?"

        btn["command"]=Delete_file()

for i in range(250):

    MEMEZ()

    tkint()

    Delete_file()

mainloop()











