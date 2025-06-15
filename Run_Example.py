from customlib import *

async def main():
await gyro_straight(15, vel=550, forward_or_backward=1)
#distance in cm
#forward 1; backward -1
await turn(-1,  spin_or_pivot=2, 45, 300, 150)
#left -1; right 1
#spin 2; pivot 1
#vel use 300-600
#acc use 100-400
await motor.run_for_degrees(attachment_right, 90, 300)
await gyro_straight(10, vel=550, forward_or_backward=-1)

runloop.run(main())
