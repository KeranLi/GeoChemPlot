#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import tkinter.ttk as ttk
from dataloader import FileSelector
from Analysis_tool.rare_earth_element import Normalization

class Main_GUI(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Geochemistry Analysis: Major and Trace')
        self.master.geometry("800x400")  # 设置窗口大小
        self.master.minsize(width=800, height=600)  # 设置窗口的最小尺寸
        self.pack()
        self.path = StringVar()
        self.txts = []
        self.createWidget()

    def createWidget(self):
        # First row
        self.btn11 = Button(self, text='File path', width=15, command=self.select_file)
        self.btn11.grid(row=0, column=0)
        self.logo_label = Label(self, text='Major and Trace Elements Analysis', font=('Arial', 10, 'bold'))
        self.logo_label.grid(row=0, column=1, columnspan=3, rowspan=2)
        self.btn13 = Button(self, text='Help', width=15)
        self.btn13.grid(row=0, column=4, padx=0)
        # 第2排
        self.label31 = Label(self, text='The choosen path:', width=15, relief='flat', anchor='e',)
        self.label31.grid(row=2, column=0, pady=20)
        self.label32 = Label(self, textvariable= self.path, width=50, anchor='w')
        self.label32.grid(row=2, column=1, columnspan=3)
        self.label33 = Label(self, text='The Normalized Method is:', width=15, relief='flat', anchor='e',)
        self.label33.grid(row=2, column=2, columnspan=3)
        #第3排
        self.label41 = Label(self, text='Sample name', width=15, relief='flat', anchor='e', )
        self.label41.grid(row=4, column=1, pady=10)
        self.wenjianming_name = Entry(self)
        self.wenjianming_name.grid(row=4, column=2)
        #第4排
        self.btn51 = Button(self,text='Start', width=15, command=self.data_analysis)
        self.btn51.grid(row=4, column=3, columnspan=2,pady=40)
        # self.btn52 = Button(self, text='退出', width=15, command= self.quit_system)
        # self.btn52.grid(row=4, column=3)
        # 第5排
        self.pb = ttk.Progressbar(self, length=200, mode = 'indeterminate', orient= HORIZONTAL)
        self.pb.grid(row=5, column=1, pady=20, columnspan=3)
        self.pb['value'] = 0
        self.pb['maximum'] = 100
        self.pb.start()
        # self.pb.stop()
        # 第5排
        self.label61 = Label(self, text='Author: Keran Li', width=20, font=('Helvetic', 15, 'bold'), relief= 'ridge', fg='black', )
        self.label61.grid(row=6, column=1, columnspan=3)

    # 选择文件
    def select_file(self):
        self.selectTxts = FileSelector.selectTxts(self)

    def data_analysis(self):
        self.data_analysis = Normalization.data_analysis(self)