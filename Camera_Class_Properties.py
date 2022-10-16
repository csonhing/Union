from operator import truediv
from turtle import left
from Python_Camera_Control import* 
from Learning import*  


# Entry 1 (1092022) Each camera has its own created attributes. 
# The only unique attribute assigned to each one at the time of writing this are the individual IP addresses. 
# This will make issuing commands easier
# Command1 will be sent and the camera will keep moving in tha direction until it hits its limit.
# The sleep timer determines the time between command1 and command2
# Command2 will be send and it will immediately stop whatever movement command1 initiates
# In a way, the "Distance" variable will act as 

class Camera:
    # Variables = characteristics of the object
    # Functions = actions the object can take
    def _init_(self,camip,channel,startmoves,stopmoves,speed,distance):
        self.IP = camip
        self.ChanneltoSet = channel 
        self.startmovesets = startmoves
        self.stopmovesets = stopmoves
        self.DistanceToSet = distance
        self.SpeedToSet = speed
        self.command1 = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + startmoves + "\"byValue\":" + speed +"}}}" 
        time.sleep(distance)
        self.command2 = "http://"+ camip + "/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":" + channel + "\"szPtzCmd\":" + stopmoves + "\"byValue\":" + speed +"}}}" 


    def setcamip(self,IP):
        self.setcamip = list("172.31.0.67","172.31.0.69","172.31.0.68")
        if (list.__contains__(IP)):
            self.camip = IP
            return True
        else:
            return False

    def setCamSpeed(self, SpeedToSet):
        self.setCamSpeed = list(range(1, 101)) # Move this to constructor because its a constant
        if (list.__contains__(SpeedToSet)):
            self.speed = SpeedToSet
            return True
        else:
            return False

    def setCamchannel(self,ChannelToSet):
        self.setCamchannel = list(range(0, 3)) # Move this to constructor because its a constant
        if (list.__contains__(ChannelToSet)):
            self.channel = ChannelToSet
            return True
        else:
            return False

    def setCamdistance(self,DistanceToSet):
        self.setCamdistance = list(range(1, 11))
        if (list.__contains__(DistanceToSet)):
            self.distance = DistanceToSet
            return True
        else:
            return False

    def startmoves(self):
        self.left = "\"left_start\","
        self.leftup = "\"leftup_start\","
        self.leftdown = "\"leftdown_start\","
        self.right = "\"right_start\","
        self.rightup = "\"rightup_start\","
        self.rightdown = "\"rightdown_start\","
        self.up = "\"up_start\","
        self.down = "\"down_start\","
        self.zoomin = "\"zoomadd_start\","
        self.zoomout = "\"zoomdec_start\","
        self.preset = "\"preset_call\","
    
    def stopmoves(self):
        self.left = "\"left_stop\","
        self.leftup = "\"leftup_stop\","
        self.leftdown = "\"leftdown_stop\","
        self.right = "\"right_stop\","
        self.rightup = "\"rightup_stop\","
        self.rightdown = "\"rightdown_stop\","
        self.up = "\"up_stop\","
        self.down = "\"down_stop\","
        self.zoomin = "\"zoomadd_stop\","
        self.zoomout = "\"zoomdec_stop\","
        self.preset = "\"preset_call\","

    

