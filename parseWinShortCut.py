
import os
import pythoncom
from win32com.shell import shell
from win32com.shell import shellcon

def getPathFromLink(lnkpath):    
    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink, None,
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
    shortcut.QueryInterface( pythoncom.IID_IPersistFile ).Load(lnkpath) 
    path = shortcut.GetPath(shell.SLGP_RAWPATH)[0]
    return path

def main():
    print(os.listdir())
    print('hello win32con')
    print(getPathFromLink('./a.lnk'))

if __name__ == '__main__':
	main()