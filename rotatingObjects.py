#Definitions
import sys
import os
import time
import math

#We define a cube by three vectors (-> 3x3 matrix) and then use rotation matrices on this matrix.
#Then we project the three 3x3 matrix into 2D by orthonormal projection and print it

rotationsteps=100000
cubelength=10 #10 characters in the console
SimpleCubeMatrix = [[1,0,0],[0,1,0],[0,0,1]]
rotationangle=math.pi/2 #90 degrees
rotationaxis= [1,0,0]
cubechar = 'o'

def rotationmatrix(phi, rax):
    return \
    [[math.cos(phi) + rax[0]**2 *(1-math.cos(phi))],[rax[0]*rax[1]*(1-math.cos(phi) - rax[2]*math.sin(phi))],[rax[0]*rax[2]*(1-math.cos(phi)+rax[1]*math.sin(phi))]] \
    ,[[rax[1]*rax[0]*(1-math.cos(phi)) + rax[2]*math.sin(phi)],[math.cos(phi)+rax[1]**2*(1-math.cos(phi))],[rax[1]*rax[2]*(1-math.cos(phi))-rax[0]*math.sin(phi)]] \
    ,[[rax[2]*rax[1]*(1-math.cos(phi)) - rax[1]*math.sin(phi)],[rax[2]*rax[1]*(1-math.cos(phi))+rax[0]*math.sin(phi)],[math.cos(phi)+rax[2]**2 *(1-math.cos(phi))]]

#def matrixmultiplication(m1,m2)
#    return
#def rotatecube:
 #   return

#def printcube:
 #   return

clear = lambda: os.system("cls")

#Printing
for x in range(rotationsteps):
    print(str(x) + "ms")
    clear()