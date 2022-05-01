import urllib.request

webUrl= urllib.request.urlopen('http://172.31.0.66/ajaxcom?szCmd={"SysCtrl":{"PtzCtrl":{"nChanel":0,"szPtzCmd":"left_start","byValue":50}}}')
   
print("result code: " + str(webUrl.getcode()))
