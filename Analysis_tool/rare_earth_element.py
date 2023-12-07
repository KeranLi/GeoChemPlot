import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus']=False #正常显示

class Normalization:
    def __init__(self):
        self.sample_nameq

    def data_analysis(self):
        sample_name = self.wenjianming_name.get()
        #print(sample_name)
        for txt in self.txts:
            dates = pd.read_excel(txt,skiprows = 1)#读取文件，并忽略前两行
            #获取稀土配分曲线需要的行列内容
            dates.duplicated(['Unnamed: 2'])
            dates = dates.drop_duplicates(['Unnamed: 2'])
            dates = dates.loc[2:,["Unnamed: 2","Y","La","Ce","Pr","Nd","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu"]]

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
            date_XT = pd.concat(
                [
                    date_lable,
                    date_La,
                    date_Ce,
                    date_Pr,
                    date_Nd,
                    date_Sm,
                    date_Eu,
                    date_Gd,
                    date_Tb,
                    date_Dy,
                    date_Y,
                    date_Ho,
                    date_Er,
                    date_Tm,
                    date_Yb,
                    date_Lu
                ],
                axis = 1
                )  

            #分组并将每一组构建成新的DataFrame
            sample_date = date_XT.loc[date_XT['Unnamed: 2'].str.contains(sample_name)]
            df_sample_date = pd.DataFrame(sample_date)
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
