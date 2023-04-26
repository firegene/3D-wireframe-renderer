from math import cos, sin

def rotX(xyz,theta):
    xrot = xyz[1] * cos(theta) - xyz[2] * sin(theta)
    yrot = xyz[1] * sin(theta) + xyz[2] * cos(theta)
    return (xyz[0], xrot, yrot)


def rotZ(xyz,theta):
    xrot = xyz[0] * cos(theta) - xyz[1] * sin(theta)
    yrot = xyz[0] * sin(theta) + xyz[1] * cos(theta)
    return (xrot, yrot, xyz[2])


def rotY(xyz,theta):
    xrot = xyz[0] * cos(theta) - xyz[2] * sin(theta)
    yrot = xyz[0] * sin(theta) + xyz[2] * cos(theta)
    return (xrot, xyz[1], yrot)
