
import os, time
import stat as st
from parseWinShortCut import getPathFromLink

myDir = 'C:\\Users\\zcc\\AppData\\Roaming\\Microsoft\\Windows\\Recent'

def collectFiles(recentFilesDir):
    listName = os.listdir(recentFilesDir)
    rawDictRecentFiles = {}
    for n in listName:
        #print(n)
        print(n)
        try:
            lnkName = os.path.join(recentFilesDir, n)
            fullFileName = getPathFromLink(lnkName)
            stat = os.stat(lnkName)
        except Exception as e:
            print(n+'\tnot a link, pass.')
            continue
        try:
            s = os.stat(fullFileName)
            if st.S_ISDIR(s.st_mode):
                continue
        except Exception as e:
            print(fullFileName+'\tnot found, pass.')
            continue
        if rawDictRecentFiles.get(lnkName):
            if stat.st_mtime>rawDictRecentFiles[lnkName]:
                rawDictRecentFiles[lnkName] = max(stat.st_atime, stat.st_mtime, stat.st_ctime)
        else:
            rawDictRecentFiles[lnkName] = max(stat.st_atime, stat.st_mtime, stat.st_ctime)
        #print(rawDictRecentFiles[n])
    return rawDictRecentFiles

def max(a, b, c):
    d = a;
    if b>d:
        d = b
    if c>d:
        d = c
    return d

def sortFiles(recentFilesDir):
    return sorted(collectFiles(recentFilesDir).items(), key=lambda x:x[1], reverse=True)

def writeRss(recentFiles):
    output = open('a.rss', 'bw')
    ee = [
    '<?xml version="1.0" encoding="utf-8"?>',
    '<rss version="2.0">',
    '<channel>',
    '<title>'+time.strftime("%X %d-%b-%Y", time.localtime())+'</title>',
    '<link>http://www.bing.com</link>',
    '<description>Time</description>'
    ]
    for e in ee:
        output.write(e.encode('utf-8'))
        output.write('\n'.encode('utf-8'))

    for e in recentFiles:
        addItem(output, e[0])

    ee = [
    '</channel>',
    '</rss>'
    ]
    for e in ee:
        output.write(e.encode('utf-8'))
        output.write('\n'.encode('utf-8'))

    output.close()

def checkFile(file):
    if not(file.endswith('.lnk')):
        return False
    return file.count('.')>0

def addItem(output, file):
    output.write('<item>\n'.encode('utf-8'))
    output.write('<title>'.encode('utf-8'))
    f = file.encode('utf-8')
    fSplit = file.split('\\')
    fSplit.reverse()
    output.write(fSplit[0].encode('utf-8'))
    output.write('</title>\n'.encode('utf-8'))
    output.write('<link>'.encode('utf-8'))
    output.write(f)
    output.write('</link>\n'.encode('utf-8'))
    output.write('<description>'.encode('utf-8'))
    output.write(f)
    output.write('</description>\n'.encode('utf-8'))
    output.write('</item>\n'.encode('utf-8'))

def main():
    recentFiles = sortFiles(myDir)
    print('==========')
    for e in recentFiles:
        print(e[0], '\t', e[1])
    writeRss(recentFiles)

if __name__ == '__main__':
    main()