from tkinter import *
from GUI import Main_GUI
if __name__ == '__main__':
    root = Tk()

    screeenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    w = 1200
    h = 800
    x = (screeenwidth-w)/2
    y = (screenheight-h)/2 
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root.title('Geochemistry Analysis: Major and Trace')
    app = Main_GUI(master=root)
    root.mainloop()