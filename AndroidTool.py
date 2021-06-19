#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@author: Liang.Chen
@version: 2016-12-12
new
'''

from Tkinter import *
import os
# import tkMessageBox
import datetime

# def callback():
#     var.set('Thanks ! ')

def function_capture_android():
    time = datetime.datetime.now()
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # print(nowTime)
    # print(time)

    os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png  ./%s.png' % nowTime)
    # var.set('Result: Finished at %s' % datetime.datetime.today())

    #打印文件名
    var.set('Result: Success \n \n'
        'Filename: %s.png' % nowTime)

def function_install_android():
    os.system('adb install -r *.apk')
    var.set('Result: Finished at %s' % datetime.datetime.today())


def function_capture_iOS():
    time = datetime.datetime.now()
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    current_dir = os.getcwd()
    # print(current_dir)
    # print(nowTime)
    # print(time)
    # os.system('tidevice /sdcard/screenshot.png  ./%s.png' % nowTime)
    os.system('tidevice screenshot')
    # sleep(2)
    # var.set('Result: Finished at %s' % datetime.datetime.today())
    os.system('mv screenshot.jpg  %s.png' % nowTime)

    #打印文件名
    file_name = current_dir + '/' + '%s.png' % nowTime
    # print(file_name)
    var.set('Result: ==== Success ==== \n \n'
        'Save to: \n %s' % file_name)

def function_install_iOS():
    os.system('tidevice install *.ipa')
    var.set('Result: Finished at %s' % datetime.datetime.today())



def function_download_dingtone_log():
    os.system('adb pull /sdcard/Dingtone/log ./log')

def function_download_talkU_log():
    os.system('adb pull /sdcard/Talkyou/log ./log')

# 创建下拉列表的group
# li = ['* Capture Screenshot', '* Install APK', '* Log TalkU', '* Log TalkUDebug','* Log Dingtone','* Log DingtoneDebug']

win = Tk()     # 初始旷的声明
win.title('Android Tool Beta v0.9.2，2016')
content = win.command

today = datetime.date.today()
# print (today)

frame1 = Frame(win)   # 在初始框里面 声明两个模块 .
frame2 = Frame(
            master=win,  # 父容器
            # bg='blue',  # 背景颜色
            # relief='groove',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            # bd=60,  # 边框的大小
            height=100,  # 高度
            width=100,  # 宽度
            padx=10,  # 内间距，字体与边框的X距离
            pady=10,  # 内间距，字体与边框的Y距离
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            )
frame3 = Frame(
            master=win,  # 父容器
            # bg='yellow',  # 背景颜色
            # relief='groove',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            # bd=30,  # 边框的大小
            height=100,  # 高度
            width=100,  # 宽度
            padx=10,  # 内间距，字体与边框的X距离
            pady=10,  # 内间距，字体与边框的Y距离
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            )
# frame4 = Frame(win)

# 创建一个文本Label对象
var = StringVar()           #声明可变 变量
var.set("Note: "
        "Choose the command which you need.") # 设置变量 .
textLabel = Label(frame1,           # 绑定到模块1
                  textvariable=var,  # textvariable 是文本变量的意思 .
                  justify=LEFT)    # 字体位置
textLabel.pack(side=LEFT)   #  整体位置

# 创建一个下拉菜单
variable = StringVar(win)
variable.set('*** Please choose ***')
OM = OptionMenu(win, variable, '* Capture Screenshot', '* Install APK', '* Log TalkU', '* Log TalkUDebug','* Log Dingtone','* Log DingtoneDebug')
OM.pack()

# 加一个按钮
# okButton = Button(frame2, text="OK !", command=callback)  # 按下按钮 执行 callback函数
# okButton = Button(frame2, text="OK", command=callback)
# okButton.pack(side=LEFT)

CaptureButton_Android = Button(frame2, text="Android Screenshot", command=function_capture_android)
CaptureButton_Android.pack(side=LEFT)

# InstallButton_Android = Button(frame2, text="Install apk（disable）", command=function_install_android)
# InstallButton_Android.pack(side=LEFT)


CaptureButton_iOS = Button(frame3, text="iOS Screenshot", command=function_capture_iOS)
CaptureButton_iOS.pack(side=LEFT)

# InstallButton_iOS = Button(frame3, text="Install ipa（disable）", command=function_install_iOS)
# InstallButton_iOS.pack(side=LEFT)



# # 禁用
# DownloadDingtonelogButton = Button(frame2, text="Dingtone Log", command=function_download_dingtone_log)
# DownloadDingtonelogButton.pack(side=LEFT)
#
# # 禁用
# DownloadTalkUlogButton = Button(frame2, text="TalkU Log", command=function_download_talkU_log)
# DownloadTalkUlogButton.pack(side=LEFT)

frame1.pack(padx=100, pady=60)
frame2.pack(padx=20, pady=20)
frame3.pack(padx=20, pady=20)

win.resizable(0,0)  # 固定窗口的大小
win.mainloop()
