# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 09:33:19 2017

@author: zcc
"""

import tkinter as tk

root = tk.Tk()
#root.attributes("-alpha", 0.8)
root.geometry("400x800+10+10")
#root.overrideredirect(1)
root.attributes("-transparentcolor","white")
root["background"] = "white"

def mytkLabel(master):
    str_obj = tk.StringVar()
    str_obj.set("这是TKinter所支持的字符串类型")
 
    #bitmap_image = tk.BitmapImage(file = "./tmp/11.bmp")
    #normal_image = tk.PhotoImage(file = "C:\\Users\\zcc\\Desktop\\applogo.png")
    #print(type(normal_image))
    #print(normal_image)
    w = tk.Label(master,
                 #背景选项
                 #height = 5,
                 #width = 20,
                 padx=10,
                 pady=20,
                 background="blue",
                 alpha=0.5,
                 relief="ridge",
                 borderwidth=0,
                 #文本
                 text = "123456789\nabcde\nABCDEFG",
                 #textvariable = str_obj,
                 justify = "left",
                 foreground = "white",
                 underline = 4,
                 anchor = "ne",
                 #图像
                 #image = normal_image,
                 compound = "bottom",
                 #接受焦点
                 #takefocus = True,
                 #highlightbackground = "yellow",
                 #highlightcolor = "white",
                 #highlightthickness = 5
                 )
    w.pack()

def mytkText(master):
    t = tk.Text(root)
    t.insert('1.0',"text1\n")   # 插入
    t.insert('5.0',"text3\n")
    t.insert(tk.END,"text2\n") # END:这个Textbuffer的最后一个字符
    #t.delete('1.0','2.0')   # 删除
    t.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

def mytkButton(master):
    B = tk.Button(master, text="Hello,Python!", command=lambda : foo(1))
    B.configure(background='white')
    B.bind('<Enter>', handlerAdaptor(enterB, B))
    B.bind('<Leave>', handlerAdaptor(leaveB, B))
    B.pack()
    B1 = tk.Button(master, text="Hello,Python!", command=lambda : foo(1))
    B1.configure(background='white')
    B1.pack()
    
def handlerAdaptor(fun, *args):  
    '''''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''  
    return lambda event, fun=fun, args=args: fun(event, *args) 
    
def foo(k):
    print(k)
    #root.destroy()
    
def enterB(event, B):
    B.configure(text='bar', background='red')

def leaveB(event, B):
    B.configure(text='foo', background='white')

def mytkListBox(master):
    li     = ['C','python','php','html','SQL','java']
    movie  = ['CSS','jQuery','Bootstrap']
    listb  = tk.Listbox(master)          #  创建两个列表组件
    listb2 = tk.Listbox(master)
    for item in li:                 # 第一个小部件插入数据
        listb.insert(0,item)

    for item in movie:              # 第二个小部件插入数据
        listb2.insert(0,item)
    
    listb.itemconfig(2, bg='green')
    listb.itemconfig(0, foreground="purple")
    listb.pack()                    # 将小部件放置到主窗口中
    listb2.pack()

def main():
    mytkButton(root)
    

if __name__ == '__main__':
    main()
    root.mainloop()
    