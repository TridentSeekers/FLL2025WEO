#This Customlib file was written by TridentSeekers for FLL 2024-2025 Western Edge Open
# Please save this to hub slot 18
code: str = '''
#Reference https://primelessons.org/en/PyProgrammingLessons/SP3ImportingCustomLibrariesPython.pdf 
from hub import port, motion_sensor, button
import runloop, motor_pair, sys, motor, math
# Define global variables for robot
turning_degrees = 0
motor_left = port.B
motor_right = port.E
attatchment_left = port.D
attatchment_right = port.F

# robot set up
WHEEL_CIRCUMFERENCE = 5.57*math.pi #cm
motor_pair.pair(motor_pair.PAIR_1, motor_left, motor_right)
######################################################################################################################################
# Ultility Functions starts here #
######################################################################################################################################

# defining function turn_done
# Reference https://primelessons.org/en/PyProgrammingLessons/SP3GyroTurningPython.pdf
def turn_done():
    return abs(motion_sensor.tilt_angles()[0] * -0.1) > turning_degrees #Chen: Let's use Primelesson's. Keep the same reference.

# suggesting value combination: steering = 50, vel = 150
# defining gyro_straight function
# distance is the amount of cm you want the bot to travel
async def gyro_straight(distance, vel=550, forward_or_backward=1):
    # vel: wheel speed, always positive
    # err: err improves turning accurassy, value should be tested to be determined
    #forward_or_backward: 1 forward; -1 backward
    # calculating for moving/traveling degrees
    degrees = distance/WHEEL_CIRCUMFERENCE*360 
    # reset amount of degrees turned to 0
    motor.reset_relative_position(motor_left, 0) 
    motor.reset_relative_position(motor_right, 0) 
    #await runloop.until(motion_sensor.stable) # Do not use motion_sensor.stable because it will wait until stable to move but it is not good on the field
    # reseting yaw to 0
    motion_sensor.reset_yaw(0) 
    # Instead of motion_sensor.stable, use sleep_ms
    await runloop.sleep_ms(100) 
    
    while True:
        error = motion_sensor.tilt_angles()[0] * -0.1 # calculation for error/drift degree
        correction = int(forward_or_backward * error * -2) # calculation for amount you need to turn back to get back on track if you drifted
        motor_pair.move(motor_pair.PAIR_1, correction, velocity=forward_or_backward *vel) # keep moving like this until another command
        wheel_motor_degree = (abs(motor.relative_position(motor_left)) + abs(motor.relative_position(motor_right)))/2 # the degrees spun for both moving motors / 2
        if (wheel_motor_degree > degrees): # if spun more than the degrees commanded then...
            motor_pair.stop(motor_pair.PAIR_1) # stop both motors
            break # break out of the loop

async def turn(left_or_right, spin_or_pivot, degrees, vel, acc,err=2):
    global turning_degrees
    #left_or_right = -1 left; 1 right
    #spin=2; pivot=1
    turning_degrees=degrees-err
    motion_sensor.reset_yaw(0) # reseting yaw to 0
    await runloop.sleep_ms(100) # Chen: Replace the motion_sensor.stable
    motor_pair.move(motor_pair.PAIR_1, left_or_right * (spin_or_pivot * 50), velocity=vel,acceleration=acc)
    await runloop.until(turn_done)
'''
def exportProgram(): # Function to export the library code string
    import os
    global code
    os.chdir('/flash') # change directory to root
    try:
        os.remove('customlib.py') # remove any existing library file of the same name
    except:
        pass
    f = open('customlib.py', 'w+') # Create a new file customlib.py in the SPIKE hub root
    f.write(code) # Write out the library code string to the customlib.py file
    f.close()

import sys
exportProgram() # Runs the export function
sys.exit("Export complete")
