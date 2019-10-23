'''
Simulates a point orbiting around Earth
'''


from vpython import *
from math import pi
import csv

#intialize data collect
#data_vt = []

#intialize volocity plot
Vx_plot = gcurve(color=color.red)
Vy_plot = gcurve(color=color.blue)

M = 6.0e24 #mass of Earth
R = 6.378e6 #radius of Earth, in meters
G = 6.67e-11 #gravity constant in Nm^2/kg^2

h = 3.6e7 #heigt of orbit of rocket in km
m = 100 #mass of rocket for momentum calc

Earth = sphere(pos=vector(0,0,0), radius=R, color=color.blue)
#intial position of rocket
rocket_pos_init = vector(Earth.pos.x + R + h,Earth.pos.y,Earth.pos.z) #remeber that for regular orbit put h or R in place of (x,-,-)
#rocket object
rocket = sphere(pos=rocket_pos_init, radius= R / 5, color=color.white,
                make_trail=True, trail_type="points", interval=10)

v_esc = sqrt((2*G*M) / R)

#intial velocity (gravity*Mass of earth) / (radius of earth + rocket's height) 
                                            #total distance to rocket from Earth's center
v0 = sqrt((G*M)/(R+h))   #sqrt((G*M)/(R+h))  or   1.1*v_esc 

v = vector(0,v0,0)
#time of full orbit in hours from -side not maybe change to equation with the height of the orbit and have equation calc
T_circ = (2*pi*(R+h)) / v0
dt = 0.001*T_circ

#intialzie force, momentum-p, and set vector radius-r?r-hat vector
F = vector(0,0,0)
p = m*v
r = rocket.pos - Earth.pos

t=0 #time

while t < 15 * T_circ:
    rate(1000)
    #Force pulling rocket to earth
    F = -(G * M * m)/((R+mag(r)**2))*norm(r)
    p = p + (F*dt)
    v = p/m
        #plot volicity over time
    Vx_plot.plot((t,v.x))
    Vy_plot.plot((t,v.y))
    #update position
    rocket.pos = rocket.pos + v*dt
    r = rocket.pos - Earth.pos
    t += dt