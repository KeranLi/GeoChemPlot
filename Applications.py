#!/usr/bin/env python
# coding: utf-8

from tkinter import *
# from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import (askopenfiles, askopenfilenames,askdirectory)
# import time
import pandas as pd 
import numpy as np
import os  
import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体指定为简黑体
# noinspection PyInterpreter
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus']=False #正常显示-


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.path = StringVar()
        self.txts = []
        self.createWidget()
    def createWidget(self):
        # 第1排
        self.btn11 = Button(self, text='选择文件', width=15, command=self.selectTxts)
        self.btn11.grid(row=0, column=0)
        self.logo_label = Label(self, text='主微量元素分析', font=('黑体', 30, 'bold'))
        self.logo_label.grid(row=0, column=1, columnspan=3, rowspan=2)
        self.btn13 = Button(self, text='帮助', width=15)
        self.btn13.grid(row=0, column=4, padx=0)
        # 第2排
        self.label31 = Label(self, text='已选路径:', width=15, relief='flat', anchor='e',)
        self.label31.grid(row=2, column=1, pady=20)
        self.label32 = Label(self, textvariable= self.path, width=50, anchor='w')
        self.label32.grid(row=2, column=2, columnspan=3)
        #第3排
        self.label41 = Label(self, text='请输入样品名称:', width=15, relief='flat', anchor='e', )
        self.label41.grid(row=4, column=1, pady=10)
        self.wenjianming_name = Entry(self)
        self.wenjianming_name.grid(row=4, column=2)
        #第4排
        self.btn51 = Button(self,text='开始', width=15, command=self.data_analysis)
        self.btn51.grid(row=4, column=3, columnspan=2,pady=40)
        #self.btn52 = Button(self, text='退出', width=15, command= self.quit_system)
        #self.btn52.grid(row=4, column=3)
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
    def selectTxts(self):
        self.txts_name = askopenfilenames()
        self.txts = []
        for i in self.txts_name:
            self.path_name = os.path.split(i)[0]
            self.txts.append(os.path.split(i)[1]) 
        os.chdir(self.path_name)
        self.path_name = self.path_name
        self.path.set(self.path_name)
    def data_analysis(self):
        sample_name = self.wenjianming_name.get()
        #print(sample_name)
        for txt in self.txts:
            dates = pd.read_excel(txt,skiprows = 1)#读取文件，并忽略前两行
            #获取稀土配分曲线需要的行列内容
            dates.duplicated(['Unnamed: 2'])
            dates = dates.drop_duplicates(['Unnamed: 2'])
            dates = dates.loc[2:,["Unnamed: 2","Y","La","Ce","Pr","Nd","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu"]]
            #print(dates)
            #按球粒陨石计算稀土配分模式
            date_lable = dates.loc[2:,"Unnamed: 2"]
            date_La = dates.loc[2:,"La"]/38.2
            date_Ce = dates.loc[2:,"Ce"]/79.6
            date_Pr = dates.loc[2:,"Pr"]/8.83
            date_Nd = dates.loc[2:,"Nd"]/33.09
            date_Sm = dates.loc[2:,"Sm"]/5.55
            date_Eu = dates.loc[2:,"Eu"]/1.08
            date_Gd = dates.loc[2:,"Gd"]/4.66
            date_Tb = dates.loc[2:,"Tb"]/0.774
            date_Dy = dates.loc[2:,"Dy"]/4.68
            date_Y = dates.loc[2:,"Y"]/27
            date_Ho = dates.loc[2:,"Ho"]/0.991 
            date_Er = dates.loc[2:,"Er"]/2.85
            date_Tm = dates.loc[2:,"Tm"]/0.405
            date_Yb = dates.loc[2:,"Yb"]/2.82
            date_Lu = dates.loc[2:,"Lu"]/0.433
            #构建新的DateFrame
            date_XT = pd.concat([date_lable,date_La,date_Ce,date_Pr,date_Nd,date_Sm,date_Eu,date_Gd,date_Tb,
                       date_Dy,date_Y,date_Ho,date_Er,date_Tm,date_Yb,date_Lu],axis = 1)  
            
            #outputpath="D:/{}.xlsx"

            #分组并将每一组构建成新的DataFrame
            sample_date = date_XT.loc[date_XT['Unnamed: 2'].str.contains(sample_name)]
            df_sample_date = pd.DataFrame(sample_date)
            #print(df_sample_date)
            #df_sample_date.to_excel(outputpath.format(sample_name),index=False,header=True)#输出表格
            df_sample_date.to_excel(self.wenjianming_name.get()+'.xlsx',index=False,header=True)#输出表格
            idx = df_sample_date.index.tolist()
            #print(df_sample_date)
            legend_name = df_sample_date["Unnamed: 2"].tolist()
            name = list[sample_name]
            for j in idx:
                X = ["La","Ce","Pr","Nd","Sm","Eu","Gd","Tb","Dy","Y","Ho","Er","Tm","Yb","Lu"]
                Y = df_sample_date.loc[j,["La","Ce","Pr","Nd","Sm","Eu","Gd","Tb","Dy","Y","Ho","Er","Tm","Yb","Lu"]]
                plt.plot(X,Y)
                ax = plt.gca()
                ax.set_yscale('log')
                plt.legend(legend_name)
                plt.title(sample_name)
                plt.savefig(self.wenjianming_name.get()+'.svg')
