import glob
import os
import string
from tkinter import *
import tkinter as tk
import threadpool


kinds = ['.py','.c','.java','.cpp','.h']
counts=[0,0,0,0,0]
names=['C++','Java','C','H','Python']
names2=['Python','C语言','Java','C++','H']
kinds2name2={k:n for k ,n in zip(kinds,names2)}
total={}
for n in range(5):
    total[kinds[n]]={'code':names[n],'count':counts[n]}
import time
import re
def get_num_func_lines(kind,ff):
    window="*"*7

    temp_num=0
    #已嵌套几层中括号
    layer_num=0
    #函数数量
    func_count=0
    #代码行数
    lines_count=0
    #函数行数
    func_lines_count=0
    #函数行数列表
    func_lines_list=[]

    content=ff.read()
    #找到第一个括号
    func_find=False
    #找到第二个括号
    func_find_second=False
    #找到第一个中括号
    func_begin=False
    for id,ch in enumerate(content):
        #跳过换行
        if ch=='\n':
            lines_count+=1
            if func_begin:
                temp_num+=1
                func_lines_count+=1
            continue
        #跳过空格和缩进
        if ch==" " or ch=="\t":
            if window[-1]!=' 'or window[-1]!='\n' or window[-1]!='\t':
                window = window[1:] + ch
            continue

        if not func_begin:
            #函数未开始，且找到了一半括号
            if ch=='(':
                #不能为特殊函数
                func_name=re.split('\s|\n|\t',window)[-1]
                if func_name=='for' or func_name=='if' or func_name=='switch' or func_name=='catch' or func_name=='except':
                    continue
                #找到符合条件的一半括号
                func_find=True
            #更新滑动窗口
            window = window[1:] + ch
            #函数未开始且找到里另一半括号
            if func_find and ch==')':
                func_find_second=True
                continue
            #找到了所有括号且函数开始了
            if func_find_second and ch=='{':
                func_count += 1
                layer_num+=1
                func_begin=True
                func_find=False
                func_find_second=False
                continue

        #函数内部的括号不能增加函数数量，且要为其增加{个数
        if func_begin and ch=="{":
            layer_num+=1
        #避免出现运算中的小括号，如果出现了直接将括号发现置零
        if func_find_second and ch in string.punctuation:
            func_find=False
            func_find_second=False

        if func_begin and ch=="}":
            if layer_num==1:
                func_lines_list.append(temp_num)
                temp_num=0
                func_find = False
                func_find_second = False
                func_begin = False
            layer_num-=1

    return lines_count,func_count,func_lines_count,func_lines_list

def sub_count(pm):
    sub_filename_list=pm[0]
    info_list=pm[1]
    kind=pm[2]
    all_date=pm[3]
    ed_time=pm[4]
    be_time=pm[5]
    encodings=pm[6]
    for filename in sub_filename_list:
        if all_date is False and ((os.path.getmtime(filename)) >= ed_time or (os.path.getmtime(filename)) <= be_time):
            continue
        for i, encoding in enumerate(encodings):
            try:
                with open(filename, 'r', encoding=encoding) as ff:
                    result = get_num_func_lines(kind, ff)
                    info_list[0] += result[0]
                    info_list[1] += 1
                    info_list[2] += result[1]
                    info_list[3] += result[2]
                    info_list[4] = info_list[4] + result[3]
                break
            except Exception as e:
                # 如果所有编码都无法处理该文件，则建立异常文件统计异常文件名
                if i == 3:
                    with open('errorfiles.txt', 'a') as err:
                        err.write(filename + '\n')
                continue


def counts(folder_name,all_choices,be_date,ed_date,all_date):
    total_info={}
    be_date_array=time.strptime(be_date,'%Y-%m-%d')
    ed_date_array=time.strptime(ed_date,'%Y-%m-%d')
    be_time=time.mktime(be_date_array)
    ed_time=time.mktime(ed_date_array)

    kinds = ['.py', '.c', '.java', '.cpp', '.h']
    encodings=['utf-8','gbk','ISO-8859-1']
    chose_kinds=[]

    for inde,choice in enumerate(all_choices):
        if choice==1:
            chose_kinds.append(kinds[inde])


    for row,kind in enumerate(chose_kinds):
        lines_count=0
        file_count=0
        func_count=0
        func_lines_count=0
        func_lines_lit=[]

        info_list=[0,0,0,0,[]]



        filename_list=[filename for filename in glob.iglob(folder_name+'/**/*'+kind,recursive=True)]

        step=int(len(filename_list)/10)
        if step<=0:
            sub_filename_list=[filename_list]
            for i in range(9):
                sub_filename_list.append([])
        else:
            sub_filename_list=[filename_list[i:i+step] for i in range(0,len(filename_list),step)]

        parameters=[]
        for i in range(10):
            pm = [sub_filename_list[i], info_list, kind, all_date, ed_time, be_time, encodings]
            parameters.append(pm)

        pool = threadpool.ThreadPool(10)
        tasks = threadpool.makeRequests(sub_count, parameters)
        [pool.putRequest(req) for req in tasks]
        pool.wait()

        lines_count=info_list[0]
        file_count=info_list[1]
        func_count=info_list[2]
        func_lines_count=info_list[3]
        func_lines_lit=info_list[4]

        max_num=0 if len(func_lines_lit)==0 else max(func_lines_lit)
        min_num=0 if len(func_lines_lit)==0 else min(func_lines_lit)
        avg_num=0 if len(func_lines_lit)==0 else sum(func_lines_lit)/len(func_lines_lit)
        middle_num=0 if len(func_lines_lit)==0 else sorted(func_lines_lit)[int(len(func_lines_lit)/2)]
        total_info[kinds2name2[kind]]=(lines_count,file_count,func_count,func_lines_count,max_num,min_num,avg_num,middle_num)
    print(total_info)
    return total_info


