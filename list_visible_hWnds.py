# -*- coding: utf-8 -*-

import win32gui
from pprint import pprint


def get_windows(hWnd, hWnds):
    if all([win32gui.IsWindow(hWnd),
            win32gui.IsWindowVisible(hWnd),
            win32gui.GetWindowText(hWnd)]):
        cls_name = win32gui.GetClassName(hWnd)
        hWnd_name = win32gui.GetWindowText(hWnd)
        if hWnds.get(cls_name, False):
            hWnds[cls_name].append(hWnd)
        else:
            hWnds[cls_name] = [hWnd]


def child_windows(hWnd):
    hWnd_list = []
    win32gui.EnumChildWindows(hWnd,
                              lambda hWnd, param: param.append(hWnd), hWnd_list)
    return hWnd_list


def hWnd_info(hWnd):
    return dict(
        id=hWnd,
        name=win32gui.GetWindowText(hWnd),
        cls=win32gui.GetClassName(hWnd),)


hWnds_set = {}
win32gui.EnumWindows(
    lambda hWnd, param: get_windows(hWnd, param), hWnds_set)
pprint(hWnds_set)

for cls, hWnds in hWnds_set.items():
    print('=' * 80)
    print(cls)
    
    for hWnd in hWnds:
        print('-' * 80)
        pprint(hWnd_info(hWnd))
        if cls == 'Chrome_WidgetWin_1':
            for e in child_windows(hWnd):
                pprint(hWnd_info(e))

print('=' * 80)

table = {}
for j, hWnd in enumerate(hWnds_set['CabinetWClass']):
    info = hWnd_info(hWnd)
    print(j, info['name'])
    table[j] = info['id']

x = int(input())
print(table[x])
win32gui.SetForegroundWindow(table[x])