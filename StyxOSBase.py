# Library imports
from vex import *


# Begin project code
# Extends pneumatic piston
Index.set(False)
Endgame.set(False)




#Creates function to rectract pneumatic piston for index
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