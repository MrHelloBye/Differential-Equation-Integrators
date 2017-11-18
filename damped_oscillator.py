import matplotlib.pyplot as plt
import numpy as np

euler = False
v_verlet = True

## Standard form of the damped oscillator equation
# accel + a*vel + b*vel^2 + c*pos = d
    
##Coefficients
a, b, c, d = 0.5, 0.05, 1, 1

## Initial conditions
init_pos = 0
init_vel = 10

dt = 0.1
time = np.arange(0,50+dt,dt)

pos = [init_pos]
vel = [init_vel]

##Euler forward integration is unstable, first order and not symplectic
if euler == True:
    for i in range(len(time)-1):
        new_vel = vel[i] + (-a*vel[i]-b*vel[i]**2-c*pos[i]+d)*dt
        new_pos = pos[i] + vel[i]*dt
    
        vel.append(new_vel)
        pos.append(new_pos)


## Velocity Verlet is stable for oscillatory motion and is symplectic
## Velocity Verlet is second order accurate
elif v_verlet == True:
    
    for i in range(len(time)-1):
        
        #Calculate intermediate velocity (velocity Verlet)
        int_vel = vel[i] + dt/2*(-a*vel[i]-b*vel[i]**2-c*pos[i]+d)
        new_pos = pos[i] + dt*int_vel
        new_vel = int_vel + dt/2*(-a*int_vel-b*int_vel**2-c*new_pos+d)
    
        vel.append(new_vel)
        pos.append(new_pos)
    
    
plt.plot(time,pos,label="Position")
plt.plot(time,vel,label="Velocity")
plt.xlabel("Time")
plt.legend()
plt.savefig("Damped Oscillator a="+str(a)+" b="+str(b)+" c="+str(c)+" d="+str(d)+".pdf")
plt.show()
