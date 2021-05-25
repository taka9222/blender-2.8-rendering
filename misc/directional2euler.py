import numpy as np
import math

data_path = "path_to_degree.txt"

f = open(data_path)
lines = f.readlines()
f.close()
for line in lines:
    l = [x for x in line.split()]
    direction = np.array([float(l[0]), float(l[1]), float(l[2])])
    up = np.array([0, 1, 0])

    xaxis = np.cross(up, direction)
    xaxis_L2 = np.linalg.norm(xaxis, ord=2)
    xaxis = xaxis / xaxis_L2

    yaxis = np.cross(direction, xaxis)
    yaxis_L2 = np.linalg.norm(yaxis, ord=2)
    yaxis = yaxis / yaxis_L2

    R11, R12, R13 = xaxis[0], yaxis[0], direction[0]
    R21, R22, R23 = xaxis[1], yaxis[1], direction[1]
    R31, R32, R33 = xaxis[2], yaxis[2], direction[2]

    if R31 != 1 and R31 != -1:
        y1 = -math.asin(R31)
        y2 = math.pi - y1
        x1 = math.atan2(R32 / math.cos(y1), R33 / math.cos(y1))
        x2 = math.atan2(R32 / math.cos(y2), R33 / math.cos(y2))
        z1 = math.atan2(R21 / math.cos(y1), R11 / math.cos(y1))
        z2 = math.atan2(R21 / math.cos(y2), R11 / math.cos(y2))
        x, y, z = x1, y1, z1
    else:
        z = 0
        if R31 == -1:
            y = math.pi / 2
            x = z + math.atan2(R12, R13)
        else:
            y = -math.pi / 2
            x = -z + math.atan2(-R12, -R13) 

    print("{0}, {1}, {2}".format(x, y, z))