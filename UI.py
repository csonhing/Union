from turtle import left
from Python_Camera_Control import* 
from Learning import*  
channel = "0,"
direction = ["\"left_start\"," "\"leftup_start\"," "\"leftdown_start\"," "\"right_start\"," "\"rightup_start\"," "\"rightdown_start\"," "\"up_start\"," "\"down_start\"," "\"zoomadd_start\"," "\"zoomdec_start\"," "\"preset_call\","  ]
IPs = ["172.31.0.66" "172.31.0.67" "172.31.0.68" "172.31.0.69"]
moves = ["left" "right" "up" "down" "zoom in" "presets" "zoom out"]
speed = str(list(range(1, 101)))
x = 2

#This controls the left movement and will move based on the camera selected, directed and speed
if "left":
    direction = "\"left_start\","
    speed == "user input somehow with a slide bar or something"
    if IPs == "172.31.0.67":
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        leftmovestart4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            leftmovestart5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                leftmovestart6(x,command)
    
    direction = "\"leftup_start\","
    speed == "user input somehow with a slide bar or something"
    if IPs == "172.31.0.67":
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        leftupmovestart4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            leftupmovestart5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                leftupmovestart6(x,command)
                
    direction = "\"leftdown_start\","
    speed == "user input somehow with a slide bar or something"
    if IPs == "172.31.0.67":
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        leftdownmovestart4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            leftdownmovestart5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                leftdownmovestart6(x,command)

#This is used for moveing the cameras in the 'right' direction
if "right":
    direction = "\"right_start\","
    speed == "user input somehow with a slide bar or something"
    if IPs == "172.31.0.67":
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        rightmovestart4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            rightmovestart5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                rightmovestart6(x,command)
    
    direction = "\"rightup_start\","
    speed == "user input somehow with a slide bar or something"
    if IPs == "172.31.0.67":
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        rightupmovestart4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            rightupmovestart5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                rightupmovestart6(x,command)
                
    direction = "\"rightdown_start\","
    speed == "user input somehow with a slide bar or something"
    if IPs == "172.31.0.67":
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        rightdownmovestart4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            rightdownmovestart5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                rightdownmovestart6(x,command)

#Code for moving the camera up
if "up":
    direction = "\"up_start\","
    speed == "user input somehow with a slide bar or something"
    if IPs == "172.31.0.67":
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        upmovestart4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            upmovestart5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                upmovestart6(x,command)

#Code for moving the camera down
if "down":
    direction = "\"down_start\","
    speed == "user input somehow with a slide bar or something"
    if IPs == "172.31.0.67":
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        downmovestart4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            downmovestart5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                downmovestart6(x,command)

#Code for calling Presets 
if "presets":
    direction = "\"preset_call\"," 
    speed == "user input somehow with a slide bar or something" #Here this will be the preset shots that you want to take; range is [0,254]
    if IPs == "172.31.0.67":   
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        presets4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            presets5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                presets5(x,command)

#Code for zooming in 
if "zoom in":
    direction = "\"zoomadd_start\","
    speed == "user input somehow with a slide bar or something" #Speed controls the zoom range
    if IPs == "172.31.0.67":   
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        zoom_in4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            zoom_in5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                zoom_in6(x,command)

#Code for zooming out
if "zoom out":
    direction = "\"zoomdec_start\","
    speed == "user input somehow with a slide bar or something" #Speed controls the zoom range
    if IPs == "172.31.0.67":   
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
        zoom_out4(x,command)
    else:
        if IPs == "172.31.0.69":
            camip  = "172.31.0.69"
            command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
            zoom_out5(x,command)
        else:
            if IPs == "172.31.0.68":
                camip  = "172.31.0.68"
                command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
                zoom_out6(x,command)
