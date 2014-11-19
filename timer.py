#!/usr/bin/python
#coding:utf-8
# FileName: simple.py
import os
import re
import sys
import time
import webbrowser

while 1:
    NowTime=time.strftime("%H:%M:%S", time.localtime())
    if NowTime == "17:31:00":
        webbrowser.open("http://kq.neusoft.com/index.jsp")
        time.sleep(1)
        continue
    if NowTime == "08:20:00":
        webbrowser.open("http://kq.neusoft.com/index.jsp")
        time.sleep(1)
        continue
        
