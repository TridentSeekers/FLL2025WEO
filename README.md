# FLL2025WEO
This Customlib file was written by TridentSeekers for FLL 2024-2025 Western Edge Open

Workflow:
1. Modifiy ExportCustomlib.py where the port settings
   motor_left = port.B
   motor_right = port.E
   attatchment_left = port.D
   attatchment_right = port.F
   WHEEL_CIRCUMFERENCE = 5.57*math.pi #cm
2. Run this file in Spike Prime and save to slot 18.
3. Test with Run_Test.py. You can use gyro_straight(), turn()
