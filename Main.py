from tkinter import *
from Applications import Application
if __name__ == '__main__':
    root = Tk()

    screeenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    w = 600
    h = 400
    x = (screeenwidth-w)/2
    y = (screenheight-h)/2 
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root.title('主微量元素分析程序')
    app = Application(master=root)
    root.mainloop()