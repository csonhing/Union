from multiprocessing.connection import wait
import urllib.request
import time
import sys

def leftmovestart():
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"left_start","byValue":50}}}')
    time.sleep(2)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"left_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def rightmovestart():
    webUrl= urllib.request.urlopen('http://172.31.0.66/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"right_start","byValue":50}}}')
    time.sleep(2)
    webUrl= urllib.request.urlopen('http://172.31.0.66/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"right_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def upmovestart():
    webUrl= urllib.request.urlopen('http://172.31.0.66/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"up_start","byValue":50}}}')
    time.sleep(2)
    webUrl= urllib.request.urlopen('http://172.31.0.66/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"up_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def downmovestart():
    webUrl= urllib.request.urlopen('http://172.31.0.66/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"down_start","byValue":50}}}')
    time.sleep(2)
    webUrl= urllib.request.urlopen('http://172.31.0.66/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"down_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def presets():
    webUrl= urllib.request.urlopen('http://172.31.0.66/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"preset_set","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def zoom_in():
    webUrl= urllib.request.urlopen('http://172.31.0.66/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomadd_stop","byValue":50}}}')
    time.sleep(2)
    return print("result code: " + str(webUrl.getcode()))


