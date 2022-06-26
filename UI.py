from Python_Camera_Control import* 

cam = input('What camera do you want to move?\n')
if cam == '4':
    z = input('How far do you want to move?\n')
    y = input('How fast do you want to move?\n')
    rightmovestart4(float(z))
elif cam == '5':
    z = input('How far do you want to move?\n')
    rightmovestart5(float(z))
elif cam == '6':
    z = input('How far do you want to move?\n')
    rightmovestart6(float(z))  
