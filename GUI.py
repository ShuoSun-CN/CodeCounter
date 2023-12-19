import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from ttkbootstrap import Style
from ttkbootstrap import DateEntry
style=Style()
root_window=style.master
root_window.title("统计代码")
root_window.geometry("1500x600")
from count_lines import counts

result_exists=None


def count_lines_gui(path,get_values,date1,date2,all_date,root_window2):
    global result_exists
#清空统计布局防止错版
    for i in range(7):
        ln = tk.Label(root_window, text='')
        ln.grid(row=14+i, column=0, columnspan=2, rowspan=6, sticky=E + W+N+S)
        ln2 = tk.Label(root_window, text='')
        ln2.grid(row=14 + i, column=2, columnspan=2, rowspan=6, sticky=E + W+N+S)
        ln3 = tk.Label(root_window, text='')
        ln3.grid(row=14 + i, column=4, columnspan=2, rowspan=6, sticky=E + W+N+S)
    #未选择路径时，提出报错
    if path =='':
        messagebox.showinfo(title='你想干嘛？', message='文件夹都不选\n全统计你想累死我是吧？')
    #未选择统计类型，提出报错
    elif max(get_values)==0:
        messagebox.showinfo(title='你又想干嘛？', message='类型都不选\n我给你统计个锤子？')
    else:
        #获取统计信息
        total_info=counts(path,get_values,date1,date2,all_date)
        result_exists=total_info
        #画出表格头部
        ln_head = tk.Label(root_window, text="语言类型",relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
        ln_head.grid(row=14, column=0,columnspan=2,sticky=E+W)
        ln2_head = tk.Label(root_window, text="代码行数",relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
        ln2_head.grid(row=14, column=2,columnspan=2,sticky=E+W)
        ln3_head = tk.Label(root_window, text="文件个数",relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
        ln3_head.grid(row=14, column=4,columnspan=2,sticky=E+W)
        ln4_head = tk.Label(root_window, text="函数个数",relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
        ln4_head.grid(row=14, column=6,columnspan=2,sticky=E+W)
        ln5_head = tk.Label(root_window, text="函数行数",relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
        ln5_head.grid(row=14, column=8,columnspan=4,sticky=E+W)
        ln5_head = tk.Label(root_window, text="最大函数行数",relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
        ln5_head.grid(row=14, column=12,columnspan=2,sticky=E+W)
        ln5_head = tk.Label(root_window, text="最小函数行数",relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
        ln5_head.grid(row=14, column=14,columnspan=2,sticky=E+W)
        ln5_head = tk.Label(root_window, text="函数行数平均值",relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
        ln5_head.grid(row=14, column=16,columnspan=2,sticky=E+W)
        ln5_head = tk.Label(root_window, text="函数行数中位数",relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
        ln5_head.grid(row=14, column=18,columnspan=2,sticky=E+W)

        #画出代码统计数量
        for row, kind in enumerate(total_info):
            ln = tk.Label(root_window, text=kind,relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
            ln.grid(row=row+15, column=0,columnspan=2,sticky=E+W)
            ln2 = tk.Label(root_window, text=total_info[kind][0],relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
            ln2.grid(row=row+15, column=2,columnspan=2,sticky=E+W)
            ln3 = tk.Label(root_window, text=total_info[kind][1],relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
            ln3.grid(row=row + 15, column=4,columnspan=2,sticky=E+W)
            ln4 = tk.Label(root_window, text=total_info[kind][2],relief="sunken",borderwidth=2,font=('微软雅黑', 10,'bold'))
            ln4.grid(row=row + 15, column=6,columnspan=2,sticky=E+W)
            ln5 = tk.Label(root_window, text=total_info[kind][3], relief="sunken", borderwidth=2,
                           font=('微软雅黑', 10, 'bold'))
            ln5.grid(row=row + 15, column=8, columnspan=4, sticky=E + W)
            ln6 = tk.Label(root_window, text=total_info[kind][4], relief="sunken", borderwidth=2,
                           font=('微软雅黑', 10, 'bold'))
            ln6.grid(row=row + 15, column=12, columnspan=2, sticky=E + W)
            ln7 = tk.Label(root_window, text=total_info[kind][5], relief="sunken", borderwidth=2,
                           font=('微软雅黑', 10, 'bold'))
            ln7.grid(row=row + 15, column=14, columnspan=2, sticky=E + W)
            ln7 = tk.Label(root_window, text=total_info[kind][6], relief="sunken", borderwidth=2,
                           font=('微软雅黑', 10, 'bold'))
            ln7.grid(row=row + 15, column=16, columnspan=2, sticky=E + W)

            ln7 = tk.Label(root_window, text=total_info[kind][7], relief="sunken", borderwidth=2,
                           font=('微软雅黑', 10, 'bold'))
            ln7.grid(row=row + 15, column=18, columnspan=2, sticky=E + W)




#获取目标文件夹路径
path = tk.StringVar()
path.set("")
def get_path():
    path_=askdirectory()
    path_=path_.replace('/','\\')
    path.set(path_)


labe1 = tk.Label(root_window,text="文件夹路径:",font=('微软雅黑', 10,'bold'))
labe1.grid(row=0,column=0,rowspan=2,ipady=10,pady=5)
entry1 = tk.Entry(root_window,textvariable=path)
entry1.grid(row=0, column=1,columnspan=4,rowspan=2,sticky=E+W,pady=10)
bt_bath=Button(root_window,text="选择文件夹",command=get_path)
bt_bath.grid(row=0,column=5,rowspan=2,sticky=E+W,pady=100)


#获取统计语言类型
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
allcheck=IntVar()

check1 = Checkbutton(root_window, text="Python",font=('微软雅黑', 10,'bold'),variable = CheckVar1,onvalue=1,offvalue=0)
check2 = Checkbutton(root_window, text="C语言",font=('微软雅黑', 10,'bold'),variable = CheckVar2,onvalue=1,offvalue=0)
check3 = Checkbutton(root_window, text="Java",font=('微软雅黑', 10,'bold'),variable = CheckVar3,onvalue=1,offvalue=0)
check4 = Checkbutton(root_window, text="C++",font=('微软雅黑', 10,'bold'),variable = CheckVar4,onvalue=1,offvalue=0)
check5 = Checkbutton(root_window, text="H",font=('微软雅黑', 10,'bold'),variable = CheckVar5,onvalue=1,offvalue=0)
all_check=Checkbutton(root_window, text="全部",font=('微软雅黑', 10,'bold'),variable = allcheck,onvalue=1,offvalue=0)
check1.grid(row=2,column=1,sticky='w',rowspan=2,ipadx=15,ipady=20)
check2.grid(row=2,column=2,sticky='w',rowspan=2,ipadx=15,ipady=20)
check3.grid(row=2,column=3,sticky='w',rowspan=2,ipadx=15,ipady=20)
check4.grid(row=2,column=4,sticky='w',rowspan=2,ipadx=15,ipady=20)
check5.grid(row=2,column=5,sticky='w',rowspan=2,ipadx=15,ipady=20)
all_check.grid(row=2,column=6,sticky='w',rowspan=2,ipadx=15,ipady=20)
labe2 = tk.Label(root_window,text="语言类型:",font=('微软雅黑', 10,'bold'))
labe2.grid(row=2,column=0,rowspan=2,ipadx=15,ipady=20)


import json
def export_json(result_exists):
    if result_exists is None:
        messagebox.showinfo(title='你想干嘛？', message='还没有结果呢')
    else:
        info_list=[]
        for info in result_exists:
            ep_info={
                "语言类型":info,
                "代码行数":result_exists[info][0],
                "文件个数":result_exists[info][1],
                "函数个数":result_exists[info][2],
                "函数行数":result_exists[info][3],
                "函数最大行数":result_exists[info][4],
                "函数最小行数":result_exists[info][5],
                "函数行数均值":result_exists[info][6],
                "函数行数中位数":result_exists[info][7],
            }
            info_list.append(ep_info)
        with open("result.json",'w') as ff:
            json.dump(info_list,ff)
        messagebox.showinfo(title='', message='导出成功！')

import pandas
def export_csv(result_exists):
    if result_exists is None:
        messagebox.showinfo(title='你想干嘛？', message='还没有结果呢')
    else:
        info_dict={
            "语言类型":[],
            "代码行数":[],
            "文件个数":[],
            "函数个数":[],
            "函数行数":[],
            "函数行数最大值":[],
            "函数行数最小值":[],
            "函数行数平均值":[],
            "函数行数中位数":[]
        }
        for info in result_exists:
            for id,key in enumerate(info_dict):
                if id==0:
                    info_dict[key].append(info)
                else:
                    info_dict[key].append(result_exists[info][id-1])
        df=pandas.DataFrame(info_dict)
        df.to_csv('result.csv',index=False)
        messagebox.showinfo(title='',message='导出成功！')






def get_values():
    if allcheck.get()==1:
        all_choices=[1,1,1,1,1]
        return all_choices
    else:
        all_choices = [CheckVar1.get(), CheckVar2.get(), CheckVar3.get(),CheckVar4.get(),CheckVar5.get()]
        return all_choices

all_date=BooleanVar()
all_date_check = Checkbutton(root_window, text="选择所有日期(勾选后将会忽略下列日期选自统计所有日期)",font=('微软雅黑', 10,'bold'),variable = all_date,onvalue=True,offvalue=False)
all_date_check.grid(row=5,column=4,rowspan=2,columnspan=4)

be_date = tk.Label(root_window,text="开始日期:",font=('微软雅黑', 10,'bold'))
be_date.grid(row=5,column=0,rowspan=1)
date1 = DateEntry()
date1.grid(row=5,column=1,rowspan=3,columnspan=3)

ed_date = tk.Label(root_window,text="结束日期:",font=('微软雅黑', 10,'bold'))
ed_date.grid(row=8,column=0,rowspan=1)
date2 = DateEntry()
date2.grid(row=8,column=1,rowspan=3,columnspan=3)
b=tk.Button(root_window,text="开始统计",command=lambda :count_lines_gui(path.get(),get_values(),date1.entry.get(),date2.entry.get(),all_date.get(),root_window)).grid(row=13,column=3)
b2=tk.Button(root_window,text="导出结果为JSON文件",command=lambda :export_json(result_exists)).grid(row=13,column=4)
b3=tk.Button(root_window,text="导出结果为CSV文件",command=lambda :export_csv(result_exists)).grid(row=13,column=5)
root_window.mainloop()

