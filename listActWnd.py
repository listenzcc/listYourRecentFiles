# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:56:27 2017

@author: zcc
"""

import win32gui

titles = set()

def foo(hwnd,mouse):
    if False and win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        titles.add(win32gui.GetWindowText(hwnd))
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd):
        titles.add(win32gui.GetWindowText(hwnd))

def main():
    print('hello wnds')
    win32gui.EnumWindows(foo, 0)
    lt = [t for t in titles if t]
    lt.sort()
    for t in lt:
        print(t)

if __name__ == '__main__':
	main()