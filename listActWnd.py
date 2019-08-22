# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:56:27 2017

@author: zcc
"""

import win32gui

windows_enabled = set()
windows_visible = set()


def parse_windows(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd):
        windows_enabled.add(win32gui.GetWindowText(hwnd))

    if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd):
        windows_visible.add(win32gui.GetWindowText(hwnd))


def main():
    print('hello wnds')
    win32gui.EnumWindows(parse_windows, 0)

    for windows in [windows_enabled, windows_visible]:
        print('-' * 80)
        for j, t in enumerate(windows):
            print(j, t)


if __name__ == '__main__':
    main()
