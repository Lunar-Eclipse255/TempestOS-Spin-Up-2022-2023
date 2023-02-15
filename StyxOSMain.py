#region VEXcode Generated Robot Configuration
from vex import *
import urandom


# Brain should be defined by default
brain=Brain()


# Robot configuration code
left_motor_a = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 381, 355.59999999999997, MM, 1)
controller_1 = Controller(PRIMARY)
Index = DigitalOut(brain.three_wire_port.a)
Intake_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
Intake_motor_b = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
Intake = MotorGroup(Intake_motor_a, Intake_motor_b)
Flywheel_motor_a = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
Flywheel_motor_b = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)
Flywheel = MotorGroup(Flywheel_motor_a, Flywheel_motor_b)




# wait for rotation sensor to fully initialize
wait(30, MSEC)






# define variables used for controlling motors based on controller inputs
controller_1_left_shoulder_control_motors_stopped = True
controller_1_right_shoulder_control_motors_stopped = True
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False


# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
   global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, controller_1_left_shoulder_control_motors_stopped, controller_1_right_shoulder_control_motors_stopped, remote_control_code_enabled
   # process the controller input every 20 milliseconds
   # update the motors based on the input values
   while True:
       if remote_control_code_enabled:
          
           # calculate the drivetrain motor velocities from the controller joystick axies
           # left = axis3 + axis1
           # right = axis3 - axis1
           drivetrain_left_side_speed = controller_1.axis3.position() + controller_1.axis1.position()
           drivetrain_right_side_speed = controller_1.axis3.position() - controller_1.axis1.position()
          
           # check if the value is inside of the deadband range
           if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
               # check if the left motor has already been stopped
               if drivetrain_l_needs_to_be_stopped_controller_1:
                   # stop the left drive motor
                   left_drive_smart.stop()
                   # tell the code that the left motor has been stopped
                   drivetrain_l_needs_to_be_stopped_controller_1 = False
           else:
               # reset the toggle so that the deadband code knows to stop the left motor next
               # time the input is in the deadband range
               drivetrain_l_needs_to_be_stopped_controller_1 = True
           # check if the value is inside of the deadband range
           if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
               # check if the right motor has already been stopped
               if drivetrain_r_needs_to_be_stopped_controller_1:
                   # stop the right drive motor
                   right_drive_smart.stop()
                   # tell the code that the right motor has been stopped
                   drivetrain_r_needs_to_be_stopped_controller_1 = False
           else:
               # reset the toggle so that the deadband code knows to stop the right motor next
               # time the input is in the deadband range
               drivetrain_r_needs_to_be_stopped_controller_1 = True
          
           # only tell the left drive motor to spin if the values are not in the deadband range
           if drivetrain_l_needs_to_be_stopped_controller_1:
               left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
               left_drive_smart.spin(FORWARD)
           # only tell the right drive motor to spin if the values are not in the deadband range
           if drivetrain_r_needs_to_be_stopped_controller_1:
               right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
               right_drive_smart.spin(FORWARD)
           # check the buttonL1/buttonL2 status
           # to control Flywheel
           if controller_1.buttonL1.pressing():
               Flywheel.spin(FORWARD)
               controller_1_left_shoulder_control_motors_stopped = False
           elif controller_1.buttonL2.pressing():
               Flywheel.spin(REVERSE)
               controller_1_left_shoulder_control_motors_stopped = False
           elif not controller_1_left_shoulder_control_motors_stopped:
               Flywheel.stop()
               # set the toggle so that we don't constantly tell the motor to stop when
               # the buttons are released
               controller_1_left_shoulder_control_motors_stopped = True
           # check the buttonR1/buttonR2 status
           # to control Intake
           if controller_1.buttonR1.pressing():
               Intake.spin(FORWARD)
               controller_1_right_shoulder_control_motors_stopped = False
           elif controller_1.buttonR2.pressing():
               Intake.spin(REVERSE)
               controller_1_right_shoulder_control_motors_stopped = False
           elif not controller_1_right_shoulder_control_motors_stopped:
               Intake.stop()
               # set the toggle so that we don't constantly tell the motor to stop when
               # the buttons are released
               controller_1_right_shoulder_control_motors_stopped = True
       # wait before repeating the process
       wait(20, MSEC)


# define variable for remote controller enable/disable
remote_control_code_enabled = True


rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)
#endregion VEXcode Generated Robot Configuration


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




#Creates function to bring turn velocity to 5%
def rollerSpeed():
   drivetrain.set_turn_velocity(5, PERCENT)
   controller_1.screen.clear_screen()
   controller_1.screen.print("5% speed")


#Creates function to bring turn velocity to 50%
def driveSpeed():
   drivetrain.set_turn_velocity(50, PERCENT)
   controller_1.screen.clear_screen()
   controller_1.screen.print("50% speed")
#Creates function to rectract pneumatic piston for index
def indexCloseBurst():
   Flywheel.spin(FORWARD, 10.0, VOLT)
   wait(1, SECONDS)
   Index.set(True)
   wait(0.3, SECONDS)
   Index.set(False)
   wait(0.3, SECONDS)
   Index.set(True)
   wait(0.3, SECONDS)
   Index.set(False)
   wait(0.3, SECONDS)
   Index.set(True)
   wait(0.3, SECONDS)
   Index.set(False)
   controller_1.screen.clear_screen()
   controller_1.screen.print("index")
   Flywheel.stop()






def intakeControl():
  
  
  


   controller_1.screen.print("Intake Control")


def flywheelControl():


   controller_1.screen.clear_screen()
   controller_1.screen.print("Flywheel Control")
  






  
  






#Makes it so when L2 is pressed the pneumatic piston retracts for index
controller_1.buttonY.pressed(indexCloseBurst)
#Makes it so when right is pressed turn velocity is set to 5%
controller_1.buttonRight.pressed(rollerSpeed)
#Makes it so when left is pressed turn velocity is set to 5%
controller_1.buttonLeft.pressed(driveSpeed)


controller_1.buttonA.pressed(intakeControl)
controller_1.buttonB.pressed(flywheelControl)


      
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




