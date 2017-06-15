#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@author: Liang.Chen
@version: 2016-12-12
'''

from Tkinter import *
import os
# import tkMessageBox
import datetime

def  callback():
    var.set('Thanks ! ')

def  Capture():
    os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png')
    var.set('Result: %s' % datetime.date.today())

def  Install():
    os.system('adb install -r *.apk')

def  Download_Dingtone_log():
    os.system('adb pull /sdcard/Dingtone/log ./log')

def  Download_TalkU_log():
    os.system('adb pull /sdcard/Talkyou/log ./log')

def  Download_DingtoneDebug_log():
    os.system('adb pull /sdcard/DingtoneDebug/log ./log')

def  Download_TalkUDebug_log():
    os.system('adb pull /sdcard/TalkyouDebug/log ./log')

# 创建下拉列表的group
# li = ['* Capture Screenshot', '* Install APK', '* Log TalkU', '* Log TalkUDebug','* Log Dingtone','* Log DingtoneDebug']

win = Tk()     # 初始旷的声明
win.title('Android Tool Beta v0.9.0')
content = win.command

today = datetime.date.today()
# print (today)

frame1 = Frame(win)   # 在初始框里面 声明两个模块 .
frame2 = Frame(win)

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

CaptureButton = Button(frame2, text="Capture", command=Capture)
CaptureButton.pack(side=LEFT)

InstallButton = Button(frame2, text="Install APK", command=Install)
InstallButton.pack(side=LEFT)

DownloadDingtonelogButton = Button(frame2, text="Dingtone Log", command=Download_Dingtone_log)
DownloadDingtonelogButton.pack(side=LEFT)

DownloadDingtonelogButton = Button(frame2, text="DingtoneDebug Log", command=Download_DingtoneDebug_log)
DownloadDingtonelogButton.pack(side=LEFT)

DownloadTalkUlogButton = Button(frame2, text="TalkU Log", command=Download_TalkU_log)
DownloadTalkUlogButton.pack(side=LEFT)

DownloadTalkUlogButton = Button(frame2, text="TalkUDebug Log", command=Download_TalkUDebug_log)
DownloadTalkUlogButton.pack(side=LEFT)

frame1.pack(padx=100, pady=50)
frame2.pack(padx=60, pady=40)

win.resizable(0,0)  # 固定窗口的大小
win.mainloop()
