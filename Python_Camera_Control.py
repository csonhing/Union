from multiprocessing.connection import wait
import urllib.request
import time
import sys

# South Pole Camera 4 Moveset
def leftmovestart4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"left_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"left_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def leftupmovestart4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftup_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftup_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def leftdownmovestart4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftdown_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftdown_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def rightmovestart4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"right_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"right_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def rightupmovestart4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightup_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightup_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def rightdownmovestart4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightdown_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightdown_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def upmovestart4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"up_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"up_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def downmovestart4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"down_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"down_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def presets4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"preset_set","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def zoom_in4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomadd_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomadd_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def zoom_out4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomdec_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomdec_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def presets4(x):
    webUrl= urllib.request.urlopen('http://172.31.0.67/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"preset_call","byValue":{x}}}}'.format(x))
    return print("result code: " + str(webUrl.getcode()))

# Middle Camera 5 Moveset
def leftmovestart5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"left_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"left_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def leftupmovestart5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftup_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftup_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def leftdownmovestart5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftdown_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftdown_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def rightmovestart5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"right_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"right_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def rightupmovestart5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightup_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightup_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def rightdownmovestart5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightdown_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightdown_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def upmovestart5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"up_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"up_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def downmovestart5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"down_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"down_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def presets5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"preset_set","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def zoom_in5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomadd_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomadd_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def zoom_out5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomdec_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomdec_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def presets5(x):
    webUrl= urllib.request.urlopen('http://172.31.0.69/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"preset_call","byValue":{0}}}}'.format(x))
    return print("result code: " + str(webUrl.getcode()))

#South Pole Camera 6 Moveset
def leftmovestart6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"left_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"left_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def leftupmovestart6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftup_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftup_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def leftdownmovestart6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftdown_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"leftdown_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def rightmovestart6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"right_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"right_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def rightupmovestart6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightup_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightup_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def rightdownmovestart6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightdown_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"rightdown_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def upmovestart6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"up_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"up_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def downmovestart6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"down_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"down_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def presets6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"preset_set","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def zoom_in6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomadd_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomadd_stop","byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def zoom_out6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomdec_start","byValue":50}}}')
    time.sleep(x)
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"zoomdec_stop,"byValue":50}}}')
    return print("result code: " + str(webUrl.getcode()))

def presets6(x):
    webUrl= urllib.request.urlopen('http://172.31.0.68/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"preset_call","byValue":{0}}}}'.format(x))
    return print("result code: " + str(webUrl.getcode()))
