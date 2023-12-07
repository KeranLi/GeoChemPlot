from tkinter import *
from tkinter.filedialog import askopenfilenames
import os 

# 选择文件
class FileSelector:
   def __init__(self):
       self.txts_name = None
       self.txts = []
       self.path_name = None
       self.path = None

   def selectTxts(self):
       self.txts_name = askopenfilenames()
       self.txts = []
       for i in self.txts_name:
           self.path_name = os.path.split(i)[0]
           self.txts.append(os.path.split(i)[1]) 
       os.chdir(self.path_name)
       self.path_name = self.path_name
       self.path.set(self.path_name)