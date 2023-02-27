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




# Extends pneumatic piston
Index.set(False)
tempDisplay=0
rollerTimer=0
Flywheel.set_velocity(120, RPM)
Endgame.set(False)


#Creates function to rectract pneumatic piston for index
def indexCloseBurst():
  Flywheel.spin(FORWARD, 9, VOLT)
  wait(1.5, SECONDS)
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
controller_1.buttonA.pressed(Endgame_)
controller_1.buttonX.pressed(indexOne)




    
#Sets the speed for Roller and drive train velocity 
Intake.set_velocity(100, PERCENT)
drivetrain.set_drive_velocity(75, PERCENT)




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
def pre_autonomous():
   Intake.set_velocity(100, PERCENT)
   drivetrain.set_drive_velocity(75, PERCENT)
   drivetrain.set_drive_velocity(50, PERCENT)
 
def autonomous():
   drivetrain.drive_for(REVERSE, 50, MM, wait=False)
   Intake.spin_for(REVERSE, 290, DEGREES)
   drivetrain.drive_for(FORWARD, 200, MM)
   drivetrain.turn_for(LEFT, 30, DEGREES)
   drivetrain.drive_for(FORWARD, 410, MM)
   drivetrain.turn_for(RIGHT, 32, DEGREES)
   drivetrain.drive_for(FORWARD, 25, MM)




  




   indexAutonomous()






















 def user_control():
   Intake.set_velocity(100, PERCENT)
   drivetrain.set_drive_velocity(75, PERCENT)
   drivetrain.set_drive_velocity(50, PERCENT)




# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
  # Start the autonomous control tasks
  auton_task_0 = Thread(autonomous)
  # wait for the driver control period to end
  while( competition.is_autonomous() and competition.is_enabled() ):
      # wait 10 milliseconds before checking again
      wait( 10, MSEC )
  # Stop the autonomous control tasks
  auton_task_0.stop()




def vexcode_driver_function():
  # Start the driver control tasks
  driver_control_task_0 = Thread( user_control )




  # wait for the driver control period to end
  while( competition.is_driver_control() and competition.is_enabled() ):
      # wait 10 milliseconds before checking again
      wait( 10, MSEC )
  # Stop the driver control tasks
  driver_control_task_0.stop()








# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )





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




def pre_autonomous():
   Intake.set_velocity(100, PERCENT)
   drivetrain.set_drive_velocity(75, PERCENT)
   drivetrain.set_drive_velocity(50, PERCENT)
 
def autonomous():
   drivetrain.drive_for(REVERSE, 50, MM, wait=False)
   Intake.spin_for(REVERSE, 290, DEGREES)
   drivetrain.drive_for(FORWARD, 200, MM)
   drivetrain.turn_for(LEFT, 30, DEGREES)
   drivetrain.drive_for(FORWARD, 410, MM)
   drivetrain.turn_for(RIGHT, 32, DEGREES)
   drivetrain.drive_for(FORWARD, 25, MM)
   index_autonomous()


def user_control():
   Intake.set_velocity(100, PERCENT)
   drivetrain.set_drive_velocity(75, PERCENT)
   drivetrain.set_drive_velocity(50, PERCENT)




# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
  # Start the autonomous control tasks
  auton_task_0 = Thread(autonomous)
  # wait for the driver control period to end
  while( competition.is_autonomous() and competition.is_enabled() ):
      # wait 10 milliseconds before checking again
      wait( 10, MSEC )
  # Stop the autonomous control tasks
  auton_task_0.stop()




def vexcode_driver_function():
  # Start the driver control tasks
  driver_control_task_0 = Thread( user_control )




  # wait for the driver control period to end
  while( competition.is_driver_control() and competition.is_enabled() ):
      # wait 10 milliseconds before checking again
      wait( 10, MSEC )
  # Stop the driver control tasks
  driver_control_task_0.stop()




# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )