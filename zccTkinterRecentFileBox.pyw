# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:31:46 2017

@author: zcc
"""

import os
import time
import listRecentFiles
import tkinter as tk
from parseWinShortCut import getPathFromLink
import subprocess

root = tk.Tk()
frm = tk.Frame(root, width=0, background='red')
label = tk.Label(root,
                 anchor=tk.NW,
                 text='',
                 fg='white',
                 background='red')
#label.pack(expand=tk.YES)
label.grid(row=0, column=0, sticky=tk.W)
buttonList = []
full2shortDict = {}
short2fullDict = {}
numButtons = 0
fontStyle = '微软雅黑'

class numButtons():
    nb = 0
    def __init__(self):
        self.nb = 0
    def newButton(self):
        self.nb += 1
        return self.nb-1
    def clearNum(self):
        self.nb = 0

nB = numButtons()

recentFilesDir = 'C:\\Users\\zcc\\AppData\\Roaming\\Microsoft\\Windows\\Recent'

def rootIni(root):
    root.attributes("-alpha", 0.6)
    root.geometry("800x1055+-5+-5")
    root.overrideredirect(1)
    #root.attributes('-fullscreen', 'true')
    root.attributes("-transparentcolor","red")
    root["background"] = "red"

def mytkButton(master, s, re):
    B = tk.Button(master,
                  anchor = tk.W,
                  text = os.path.basename(s),
                  command = lambda : foo(master, s, re),
                  background = 'gray',
                  fg = 'white',
                  font=(fontStyle, 8),
                  width = 14)
    short2fullDict[os.path.basename(s)] = s
    B.bind('<Enter>', handlerAdaptor(enterB, B))
    B.bind('<Leave>', handlerAdaptor(leaveB, B))
    B.bind('<Button-3>', handlerAdaptor(rightB, B, re))
    #B.pack(expand=tk.YES, fill='both')
    #B.pack(expand=tk.YES, fill='both')
    B.grid(row=nB.newButton(), column=0, sticky=tk.W)
    return B

def clearButtonStuff():
    while buttonList:
        buttonList.pop().pack_forget()
    full2shortDict.clear()
    short2fullDict.clear()
    nB.clearNum()

def handlerAdaptor(fun, *args):  
    '''''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''  
    return lambda event, fun=fun, args=args: fun(event, *args) 

def foo(master, s, re):
    print(s)
    try:
        os.utime(full2shortDict[s], (time.time(), time.time()))
    except Exception as e:
        pass
    if not(re):
        #os.system('explorer '+s)
        try:
            os.stat(s)
        except Exception as e:
            print(e)
            return
        subprocess.Popen('explorer '+s)
        
    clearButtonStuff()
    master.pack_forget()
    master = tk.Frame(root, width=0, background='red')
    addButtons(master)
    #master.pack(side=tk.LEFT)
    master.grid(row=1, column=0, sticky=tk.W)
    #root.destroy()

def rightB(event, B, re):
    if re==1:
        print(B['text'])
        return
    print(short2fullDict[B['text']])
    ps = os.path.dirname(short2fullDict[B['text']])
    print(ps)
    try:
        os.stat(ps)
    except Exception as e:
        print(e)
        return
    subprocess.Popen('explorer '+ps)

def enterB(event, B):
    if B['text'].__len__()<20:
        w = 20
    else:
        w = 0
    B.configure(anchor=tk.E, background='gray', font=(fontStyle, 8), width=w)
    B.grid(padx=0)
    label.configure(text=short2fullDict[B['text']], fg='white', bg='black')
    root.attributes("-alpha", 1)
    root.call('wm', 'attributes', '.', '-topmost', '1')
    #print('%d %d'%(event.x_root, event.y_root))

def leaveB(event, B):
    B.configure(anchor=tk.W, background='gray', font=(fontStyle, 8), width=14)
    B.grid(padx=0)
    label.configure(text='', bg='red')
    root.attributes("-alpha", 0.6)
    root.call('wm', 'attributes', '.', '-topmost', '0')

def collectFiles(recentFilesDir):
    listName = os.listdir(recentFilesDir)
    rawDictRecentFiles = {}
    for n in listName:
        #print(n)
        print(n)
        try:
            fullFileName = getPathFromLink(os.path.join(recentFilesDir, n))
            stat = os.stat(os.path.join(recentFilesDir, n))
        except Exception as e:
            print(n+'\tnot a link, pass.')
            continue
        try:
            os.stat(fullFileName)
        except Exception as e:
            print(fullFileName+'\tnot found, pass.')
            continue
        if rawDictRecentFiles.get(fullFileName):
            if stat.st_mtime>rawDictRecentFiles[fullFileName]:
                rawDictRecentFiles[fullFileName] = stat.st_mtime
        else:
            rawDictRecentFiles[fullFileName] = stat.st_mtime
        #print(rawDictRecentFiles[n])
    return rawDictRecentFiles

def sortFiles(recentFilesDir):
    return sorted(collectFiles(recentFilesDir).items(),
                  key=lambda x:x[1],
                  reverse=True)

def addButtons(master):
    recentFiles = listRecentFiles.sortFiles(recentFilesDir)
    print('================')
    #buttonList = []
    B = mytkButton(master,
                   time.strftime("%X %d-%b-%Y", time.localtime()),
                   1)
    buttonList.append(B)
    k = 0
    for e in recentFiles:
        k += 1
        if k==11:
            pass#break
        fullFileName = getPathFromLink(e[0])
        print(fullFileName, '\t', e[1])
        B = mytkButton(master, fullFileName, 0)
        buttonList.append(B)
        full2shortDict[fullFileName] = e[0]
    return buttonList

def main():
    print(time.strftime("%X %d-%b-%Y", time.localtime()))
    print('hello zcc')
    rootIni(root)
    addButtons(frm)

if __name__ == '__main__':
    main()
    #w, h = root.maxsize()
    #root.geometry('{}x{}+-0+-0'.format(w, h))
    #frm.pack(side=tk.LEFT)
    frm.grid(row=1, column=0, sticky=tk.W)
    root.mainloop()