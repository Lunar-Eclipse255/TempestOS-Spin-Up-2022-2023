# Library imports
from vex import *


# Begin project code
# Extends pneumatic piston
Index.set(False)
Endgame.set(False)




#Creates function to retract pneumatic piston for index
def index_close_burst():
  Flywheel.spin(FORWARD, 9, VOLT)
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




def index_autonomous():
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




def index_far():
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




def skills():
   Intake.set_velocity(1000000, PERCENT)
   drivetrain.drive_for(REVERSE, 50, MM, wait=False)
   Intake.spin_for(REVERSE, 580, DEGREES)
   drivetrain.drive_for(FORWARD,130, MM)
   drivetrain.turn_for(LEFT, 5, DEGREES)
   drivetrain.drive_for(FORWARD, 460, MM)
   drivetrain.turn_for(LEFT, 38, DEGREES)
   drivetrain.drive_for(REVERSE, 800, MM, wait=False)
   Intake.spin_for(REVERSE, 1900, DEGREES)
   drivetrain.set_drive_velocity(50, PERCENT)
   drivetrain.drive_for(FORWARD, 200, MM)
   drivetrain.turn_for(RIGHT, 80, DEGREES)
   Intake.spin_for(FORWARD,1500,DEGREES,wait=False)
   drivetrain.drive_for(REVERSE, 685, MM)
   drivetrain.drive_for(FORWARD, 350, MM)
   drivetrain.turn_for(RIGHT, 68, DEGREES)
   Intake.spin_for(REVERSE,600,DEGREES)
   Intake.spin(FORWARD)
   drivetrain.drive_for(FORWARD, 1350, MM)
   Intake.stop()
   Intake.spin_for(REVERSE,300,DEGREES)
   drivetrain.turn_for(RIGHT, 10, DEGREES)
   index_close_burst()
   drivetrain.turn_for(RIGHT, 34.5, DEGREES)
   Endgame.set(True)




def endgame():
   Endgame.set(True)




def index_one():
   Flywheel.spin(FORWARD,9, VOLT)
   wait(3, SECONDS)
   Index.set(True)
   wait(0.5, SECONDS)
   Index.set(False)
   controller_1.screen.clear_screen()
   controller_1.screen.print("index")
   Flywheel.stop()




#Programs the face buttons
controller_1.buttonY.pressed(index_close_burst)
controller_1.buttonB.pressed(index_far)
controller_1.buttonUp.pressed(skills)
controller_1.buttonLeft.pressed(endgame)
controller_1.buttonX.pressed(index_one)


#Sets the robot's different velocities
Intake.set_velocity(10000000, PERCENT)
Flywheel.set_velocity(1000000, PERCENT)
drivetrain.set_drive_velocity(75, PERCENT)
drivetrain.set_drive_velocity(50, PERCENT)


#Reverses the values of two motors
right_motor_a = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)