from turtle import left
from Python_Camera_Control import* 
from Learning import*  
channel = "0,"
direction = ["\"left_start\"," "\"leftup_start\"," "\"leftdown_start\"," "\"right_start\"," "\"rightup_start\"," "\"rightdown_start\"," "\"up_start\"," "\"down_start\"," "\"zoomadd_start\"," "\"zoomdec_start\"," "\"preset_call\","  ]
IPs = ["172.31.0.66" "172.31.0.67" "172.31.0.68" "172.31.0.69"]
speed = str(tuple(range(1, 100, 1)))
x = 2
command = "blank"

if left:
    direction = "\"left_start\","
    speed = #user input somehow with a slide bar or something
    if IPs == "172.31.0.67":
        leftmovestart4(x,command)
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
    else:
        if IPs == "172.31.0.69":
        leftmovestart5(x,command)
        camip  = "172.31.0.67"
        command = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + direction + "\"byValue\":" + speed +"}}}"
