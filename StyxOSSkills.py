# ------------------------------------------
#
#   Project:      VEXcode Project
#   Author:       VEX
#   Created:
#   Description:  VEXcode V5 Python Project
#
# ------------------------------------------




# Library imports
from vex import *




# Begin project code
# Extends pneumatic piston
Index.set(False)
tempDisplay=0
rollerTimer=0
Flywheel.set_velocity(120, RPM)
Endgame.set(False)






#Creates function to rectract pneumatic piston for index
def indexCloseBurst():
  Flywheel.spin(FORWARD, 10, VOLT)
  wait(3, SECONDS)
  Index.set(True)
  wait(0.5, SECONDS)
  Index.set(False)
  wait(0.5, SECONDS)
  Index.set(True)
  wait(0.5, SECONDS)
  Index.set(False)
  wait(0.5, SECONDS)
  Index.set(True)
  wait(0.5, SECONDS)
  Index.set(False)
  controller_1.screen.clear_screen()
  controller_1.screen.print("index")
  Flywheel.stop()


def indexAutonomous():
   Flywheel.spin(FORWARD, 12.0, VOLT)
   wait(5, SECONDS)
   Index.set(True)
   wait(0.5, SECONDS)
   Index.set(False)
   wait(0.5, SECONDS)
   Index.set(True)
   wait(0.5, SECONDS)
   Index.set(False)
   wait(0.5, SECONDS)
   controller_1.screen.clear_screen()
   controller_1.screen.print("index")
   Flywheel.stop()


def indexFar():
   Flywheel.spin(FORWARD, 12.0, VOLT)
   wait(5, SECONDS)
   Index.set(True)
   wait(0.5, SECONDS)
   Index.set(False)
   wait(0.5, SECONDS)
   Index.set(True)
   wait(0.5, SECONDS)
   Index.set(False)
   wait(0.5, SECONDS)
   Index.set(True)
   wait(0.5, SECONDS)
   Index.set(False)
   controller_1.screen.clear_screen()
   controller_1.screen.print("index")
   Flywheel.stop()
def Skills():
   drivetrain.drive_for(REVERSE, 50, MM, wait=False)
   Intake.spin_for(REVERSE, 580, DEGREES)
   drivetrain.drive_for(FORWARD,130, MM)
   drivetrain.turn_for(LEFT, 5, DEGREES)
   drivetrain.drive_for(FORWARD, 460, MM)
   drivetrain.turn_for(LEFT, 39, DEGREES)
   drivetrain.drive_for(REVERSE, 800, MM, wait=False)
   Intake.spin_for(REVERSE, 1900, DEGREES)
   drivetrain.set_drive_velocity(50, PERCENT)
   drivetrain.drive_for(FORWARD, 200, MM)
   drivetrain.turn_for(RIGHT, 80, DEGREES)
   Intake.spin_for(FORWARD,1500,DEGREES,wait=False)
   drivetrain.drive_for(REVERSE, 685, MM)
   drivetrain.drive_for(FORWARD, 350, MM)
   drivetrain.turn_for(RIGHT, 70, DEGREES)
   Intake.spin_for(REVERSE,600,DEGREES)
   Intake.spin(FORWARD)
   drivetrain.drive_for(FORWARD, 1350, MM)
   Intake.stop()
   drivetrain.turn_for(RIGHT, 11, DEGREES)
   Intake.spin_for(REVERSE,200,DEGREES)
   indexCloseBurst()
   drivetrain.turn_for(RIGHT, 40, DEGREES)
   Endgame.set(True)


def Endgame_():
   Endgame.set(True)


def indexOne():
   Flywheel.spin(FORWARD,10, VOLT)
   wait(5, SECONDS)
   Index.set(True)
   wait(0.5, SECONDS)
   Index.set(False)
   controller_1.screen.clear_screen()
   controller_1.screen.print("index")
   Flywheel.stop()




#Makes it so when L2 is pressed the pneumatic piston retracts for index
controller_1.buttonY.pressed(indexCloseBurst)
controller_1.buttonB.pressed(indexFar)
controller_1.buttonUp.pressed(Skills)
controller_1.buttonA.pressed(Endgame_)
controller_1.buttonX.pressed(indexOne)




    
#Sets the speed for Roller and drive train velocity 
Intake.set_velocity(100, PERCENT)
drivetrain.set_drive_velocity(75, PERCENT)
drivetrain.set_drive_velocity(50, PERCENT)




#Reverses the values of two motors
right_motor_a = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)




Intake.set_velocity(100, PERCENT)
Flywheel.set_velocity(100, PERCENT)




Intake.set_velocity(10000000, PERCENT)
Flywheel.set_velocity(1000000, PERCENT)


