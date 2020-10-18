#Definitions
import sys
import os
import math
import numpy as np

#We define a cube by three vectors (-> 3x3 matrix) and then use rotation matrices on this matrix.
#Then we project the  3x3 matrix into 2D and print it

rotationsteps=1
phiangle=5*(2*3.14)/360
cubelength=10 #10 characters in the console
SimpleCubeMatrix = np.array([[1,0,0],[0,1,0],[0,0,1]])
rotationangle=math.pi/2 #90 degrees
rotationaxis= [1,0,0]
pointchar = 'o'

def rotationmatrix(phi, rax): #rax: rotationaxis
    return np.array( \
    [[math.cos(phi) + rax[0]**2 *(1-math.cos(phi))], \
     [rax[0]*rax[1]*(1-math.cos(phi) - rax[2]*math.sin(phi))], \
     [rax[0]*rax[2]*(1-math.cos(phi)+rax[1]*math.sin(phi))]] \
    ,[[rax[1]*rax[0]*(1-math.cos(phi)) + rax[2]*math.sin(phi)], \
      [math.cos(phi)+rax[1]**2*(1-math.cos(phi))], \
      [rax[1]*rax[2]*(1-math.cos(phi))-rax[0]*math.sin(phi)]] \
    ,[[rax[2]*rax[1]*(1-math.cos(phi)) - rax[1]*math.sin(phi)], \
      [rax[2]*rax[1]*(1-math.cos(phi))+rax[0]*math.sin(phi)], \
      [math.cos(phi)+rax[2]**2 *(1-math.cos(phi))]])

    
def getprintstring(dimensionx,dimensiony,vectorlist, pointchar, emptychar=" "):
    #at first build the matrix with the inputs then print the stringmatrix into a console string
    stringmatrix = np.array([dimensionx,dimensiony])
    stringmatrix.fill(emptychar)
    #insert vector points
    for v in vectorlist:
        stringmatrix[v[0],v[1]] = pointchar
    stringbuilder=""
    for y in range(0, dimensionx):
        for x in range(0,dimensiony):
            stringbuilder += str(stringmatrix[x,y]*100)
        stringbuilder += "\n"
    return stringbuilder
                                

for x in range(0,rotationsteps):
    vectorlist = [[]]
    for v in range(0,3):
        SimpleCubeMatrix[v,:] = np.matmul(rotationmatrix(phiangle,rotationaxis),np.array(SimpleCubeMatrix[v,:]))
        vectorlist.append(SimpleCubeMatrix[v,:])
    printf(getprintstring(100,100,vectorlist, "x", " "))