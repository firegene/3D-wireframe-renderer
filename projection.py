def xprojected(xyz, focal):
    return (focal * xyz[0]) / (focal + xyz[2])

def yprojected(xyz,focal):
    return (focal * xyz[1]) / (focal + xyz[2])
