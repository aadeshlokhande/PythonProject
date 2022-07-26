from tkinter import * 
import tkinter.messagebox
#import stdDatabase

def _init_(self, root):
    self.root =root
    self.root.title ("Students Database Management Systems")
    self.root.geometry("1350x750+0+0")
    self.root.config(bg="cadet blue")
    StdID = StringVar ()
    Firstname = StringVar ()
    Surname = StringVar ()
    DOB = StringVar ()
    Age = StringVar ()
    Gender - StringVar ()
    Address - StringVar ()
    Mobile = StringVar() 

    # FRAMES                                                                   
    MainFrame = Frame (self.root, bg="cadet blue")
