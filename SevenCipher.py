#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Dec 16, 2018 10:31:34 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import SevenCipher_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    SevenCipher_support.set_Tk_var()
    top = Seven_Cipher (root)
    SevenCipher_support.init(root, top)
    root.iconbitmap('7cipher_icon.ico')
    root.mainloop()

w = None
def create_Seven_Cipher(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    SevenCipher_support.set_Tk_var()
    top = Seven_Cipher (w)
    SevenCipher_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Seven_Cipher():
    global w
    w.destroy()
    root.destroy()
    w = None


class Seven_Cipher:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("624x181+482+209")
        top.title("Seven Cipher")
        top.configure(background="#000000")



        self.Entry_DataPath = Entry(top)
        self.Entry_DataPath.place(relx=0.1, rely=0.31, relheight=0.11
                , relwidth=0.71)
        self.Entry_DataPath.configure(background="#595959")
        self.Entry_DataPath.configure(disabledforeground="#a3a3a3")
        self.Entry_DataPath.configure(font="TkFixedFont")
        self.Entry_DataPath.configure(foreground="#ffffff")
        self.Entry_DataPath.configure(highlightcolor="#ffffff")
        self.Entry_DataPath.configure(insertbackground="#ffffff")
        self.Entry_DataPath.configure(textvariable=SevenCipher_support.DataPath)
        self.Entry_DataPath.configure(width=444)

        self.Entry_KeyPath = Entry(top)
        self.Entry_KeyPath.place(relx=0.1, rely=0.12, relheight=0.11
                , relwidth=0.71)
        self.Entry_KeyPath.configure(background="#595959")
        self.Entry_KeyPath.configure(disabledforeground="#a3a3a3")
        self.Entry_KeyPath.configure(font="TkFixedFont")
        self.Entry_KeyPath.configure(foreground="#ffffff")
        self.Entry_KeyPath.configure(highlightbackground="#d9d9d9")
        self.Entry_KeyPath.configure(highlightcolor="#ffffff")
        self.Entry_KeyPath.configure(insertbackground="#ffffff")
        self.Entry_KeyPath.configure(selectbackground="#c4c4c4")
        self.Entry_KeyPath.configure(selectforeground="black")
        self.Entry_KeyPath.configure(textvariable=SevenCipher_support.keyPath)
        self.Entry_KeyPath.configure(width=444)

        self.Text_Data = Text(top)
        self.Text_Data.place(relx=0.02, rely=0.5, relheight=0.35, relwidth=0.79)
        self.Text_Data.configure(background="#595959")
        self.Text_Data.configure(font="TkTextFont")
        self.Text_Data.configure(foreground="#ffffff")
        self.Text_Data.configure(highlightbackground="#d9d9d9")
        self.Text_Data.configure(highlightcolor="#ffffff")
        self.Text_Data.configure(insertbackground="#ffffff")
        self.Text_Data.configure(selectbackground="#c4c4c4")
        self.Text_Data.configure(selectforeground="black")
        self.Text_Data.configure(width=494)
        self.Text_Data.configure(wrap=WORD)
        self.Text_Data.bind('<FocusIn>',lambda e:SevenCipher_support.UpdateDataText(self.Text_Data))

        self.Button_Decrypt = Button(top)
        self.Button_Decrypt.place(relx=0.83, rely=0.5, height=24, width=97)
        self.Button_Decrypt.configure(activebackground="#000000")
        self.Button_Decrypt.configure(activeforeground="white")
        self.Button_Decrypt.configure(activeforeground="#000000")
        self.Button_Decrypt.configure(background="#000000")
        self.Button_Decrypt.configure(command=SevenCipher_support.DecryptData)
        self.Button_Decrypt.configure(disabledforeground="#a3a3a3")
        self.Button_Decrypt.configure(foreground="#ffffff")
        self.Button_Decrypt.configure(highlightbackground="#d9d9d9")
        self.Button_Decrypt.configure(highlightcolor="black")
        self.Button_Decrypt.configure(pady="0")
        self.Button_Decrypt.configure(text='''Decrypt''')

        self.Button_Encrypt = Button(top)
        self.Button_Encrypt.place(relx=0.83, rely=0.66, height=24, width=97)
        self.Button_Encrypt.configure(activebackground="#000000")
        self.Button_Encrypt.configure(activeforeground="white")
        self.Button_Encrypt.configure(activeforeground="#000000")
        self.Button_Encrypt.configure(background="#000000")
        self.Button_Encrypt.configure(command=SevenCipher_support.EncryptData)
        self.Button_Encrypt.configure(disabledforeground="#a3a3a3")
        self.Button_Encrypt.configure(foreground="#ffffff")
        self.Button_Encrypt.configure(highlightbackground="#d9d9d9")
        self.Button_Encrypt.configure(highlightcolor="black")
        self.Button_Encrypt.configure(pady="0")
        self.Button_Encrypt.configure(text='''Encrypt''')

        self.Label_Key = Label(top)
        self.Label_Key.place(relx=0.02, rely=0.11, height=21, width=36)
        self.Label_Key.configure(activebackground="#595959")
        self.Label_Key.configure(activeforeground="white")
        self.Label_Key.configure(activeforeground="#ffffff")
        self.Label_Key.configure(background="#000000")
        self.Label_Key.configure(disabledforeground="#a3a3a3")
        self.Label_Key.configure(foreground="#ffffff")
        self.Label_Key.configure(text='''KEY''')
        self.Label_Key.configure(width=36)

        self.Label_Data = Label(top)
        self.Label_Data.place(relx=0.02, rely=0.3, height=21, width=46)
        self.Label_Data.configure(activebackground="#595959")
        self.Label_Data.configure(activeforeground="white")
        self.Label_Data.configure(activeforeground="#ffffff")
        self.Label_Data.configure(background="#000000")
        self.Label_Data.configure(disabledforeground="#a3a3a3")
        self.Label_Data.configure(foreground="#ffffff")
        self.Label_Data.configure(highlightbackground="#d9d9d9")
        self.Label_Data.configure(highlightcolor="black")
        self.Label_Data.configure(text='''DATA''')
        self.Label_Data.configure(width=46)






if __name__ == '__main__':
    vp_start_gui()



