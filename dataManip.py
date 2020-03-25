## spectragraph, low pass, anti-aliasing, calculate big X from our time series data (DFT)  then plot the Magnitude_ThreeC_TimeSeries
# what is the amp of th ein at that time - antialiasing look at taper at Nyquist


import sys
import struct
import array
import math

## Read Data

## Rotate Data


def VectorMagnitude(x,y,z):
    return math.sqrt(x*x+y*y+z*z)


def Magnitude_ThreeC_TimeSeries(x,y,z):
    nptsx=len(x)
    nptsy=len(y)
    nptsz=len(z)
    if nptsx != nptsy:
        print("x and y of different lengths",nptsx,nptsy)
        return
    elif nptsx != nptsz:
        print("z different length than x and y",nptsx,nptsz)
        return
    i=0
    vmag=[]
    while i < nptsx:
        vmag.append(VectorMagnitude(x[i],y[i],z[i]))
        i=i+1
    return vmag




def Coordinate_Rotation_2D(x,y,theta):
#
# Coordinate Rotation about the Z-axes
# x and y are values in the original coordinate system
# theta is the rotation angle in degrees about the Z-axis
# Looking clockwise in the positive direction of the Z-axis
#
#  This can be used for other rotations, of course:
#
#   (x,y) in the call is (x,y) only for a rotation about z.
#   (x,y) in the call is (z,x) in a rotation about y.
#   (x,y) in the call is (y,z) in a rotation about x.
#   The sense of +theta is from the first input coordinate TOWARDS the seccond
#   input coordinate
    rad_theta=math.radians(theta)
    xprime=math.cos(rad_theta)*x + math.sin(rad_theta)*y
    yprime=-math.sin(rad_theta)*x + math.cos(rad_theta)*y
    return [xprime, yprime]

def Rotate_2D_TimeSeries(x,y,theta):
    nptsx=len(x)
    nptsy=len(y)
    if nptsx != nptsy:
        print("Mismatch npts",nptsx,nptsy)
        return
    xprime=[]
    yprime=[]
    i=0
    while i < nptsx:
        [xp, yp]=Coordinate_Rotation_2D(x[i],y[i],theta)
        xprime.append(xp)
        yprime.append(yp)
        i=i+1
    return [xprime, yprime]

def Global2Local_Pseudo3D_Rotation(xglobal,yglobal,zglobal,theta,alpha):
    [ylocal,ztmp]=Coordinate_Rotation_2D(yglobal,zglobal,-alpha)
    [zlocal,xlocal]=Coordinate_Rotation_2D(ztmp,xglobal,-theta)
#
#  Input: a point in the Global coordinate system
#  Output:  The same point in the Local coordinate system
#
#  The relationship between Global and Local is given by two rotation angles.
#  This assumes there is at least one axis in common between the Local and Global system
#     thus, it is only a psuedo-3D rotation.
#
#  The angle theta defines a clockwise rotation about the common axis
#      [looking in the +direction of the local version of that axis]
#  The theta rotation takes the other two axes from Local to Global
#
#  The angles were flushed out assuming you had data in the Local system and wanted it in the Global system
#
#  The angle alpha defines a clockwise rotation about one of the initially non-common axes [same convention]
#  The alpha rotation ensures that the +direction of the common axis is the same in the Local and Global system
#
#  The code as written assumes that the common axis is the Y-axis.  It might work in other cases with judicial choice
#      of the (x,y,z) order in the argument list.  Test first!
#
#  In this Global=>Local version, the sign of the angles is reversed and the alpha rotation is done first.
#
#  See Coordinate_Rotation_2D for why the argument order is the way it is in those calls
#
    return [xlocal,ylocal,zlocal]
# i want this one
def Local2Global_Pseudo3D_Rotation(xlocal,ylocal,zlocal,theta,alpha):
    [ztmp,xglobal]=Coordinate_Rotation_2D(zlocal,xlocal,theta)
    [yglobal,zglobal]=Coordinate_Rotation_2D(ylocal,ztmp,alpha)
#
#  Input: a point in the Global coordinate system
#  Output:  The same point in the Local coordinate system
#
#  The relationship between Global and Local is given by two rotation angles.
#  This assumes there is at least one axis in common between the Local and Global system
#     thus, it is only a psuedo-3D rotation.
#
#  The angle theta defines a clockwise rotation about the common axis
#      [looking in the +direction of the local version of that axis]
#  The theta rotation takes the other two axes from Local to Global
#
#  The angles were flushed out assuming you had data in the Local system and wanted it in the Global system
#
#  The angle alpha defines a clockwise rotation about one of the initially non-common axes [same convention]
#  The alpha rotation ensures that the +direction of the common axis is the same in the Local and Global system
#
#  The code as written assumes that the common axis is the Y-axis.  It might work in other cases with judicial choice
#      of the (x,y,z) order in the argument list.  Test first!
#
#  In this Local=>Global version, the theta rotation is done first, then the alpha rotation
#
#  See Coordinate_Rotation_2D for why the argument order is the way it is in those calls.
#
    return [xglobal,yglobal,zglobal]

def Rotate_3D_TimeSeries(x,y,z,theta,alpha):
    nptsx=len(x)
    nptsy=len(y)
    nptsz=len(z)
    if nptsx != nptsy:
        print("Mismatch npts",nptsx,nptsy)
        return
    xprime=[]
    yprime=[]
    zprime=[]
    i=0
    while i < nptsx:
        [xp, yp, zp]=Local2Global_Pseudo3D_Rotation(x[i],y[i],z[i],theta,alpha)
        xprime.append(xp)
        yprime.append(yp)
        zprime.append(zp)
        i=i+1
    return [xprime, yprime, zprime]

def subtractGravity(rotate_array_z, countToGravity):
    correct = []
    for i in rotate_array_z:
        correct.append(i-countToGravity) # substracting gravity
    return correct



## Cut Data

## Export maxacc and time

## Rmean

## LowPass

## Export seismogram

## Create Equilizer
