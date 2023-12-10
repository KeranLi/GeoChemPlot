from PyQt5.QtWidgets import QFileDialog, QLineEdit
import os

class FileSelector:
   def __init__(self):
       self.txts_name = None
       self.txts = []
       self.path_name = None
       self.path = QLineEdit()

   def selectTxts(self):
       options = QFileDialog.Options()
       options |= QFileDialog.DontUseNativeDialog
       self.txts_name, _ = QFileDialog.getOpenFileNames(None, "选择文件", "", "Text Files (*.txt);;All Files (*)", options=options)
       self.txts = []
       for i in self.txts_name:
           self.path_name = os.path.split(i)[0]
           self.txts.append(os.path.split(i)[1]) 
       os.chdir(self.path_name)
       self.path_name = self.path_name
       self.path.setText(self.path_name)