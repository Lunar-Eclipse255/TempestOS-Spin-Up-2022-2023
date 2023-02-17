from vex import *
import urandom


# Brain should be defined by default
brain=Brain()


# Robot configuration code
left_motor_a = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 381, 355.59999999999997, MM, 1)
controller_1 = Controller(PRIMARY)
Endgame = DigitalOut(brain.three_wire_port.a)
Intake_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
Intake_motor_b = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)
Intake = MotorGroup(Intake_motor_a, Intake_motor_b)
Flywheel_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
Flywheel_motor_b = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
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







#Makes it so when L2 is pressed the pneumatic piston retracts for index
controller_1.buttonY.pressed(indexCloseBurst)
controller_1.buttonB.pressed(indexFar)



      
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
   # actions to do when the program starts
   brain.screen.clear_screen()
   brain.screen.print("pre-auto code")
   #Sets the speed for roller and drive train velocity  
   drivetrain.set_drive_velocity(75, PERCENT)
   #Reverses the values of two motors
  
  
def autonomous():
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_for(LEFT, 13.5, DEGREES)
    wait(0.5, SECONDS)
    indexAutonomous()
    drivetrain.turn_for(RIGHT, 29, DEGREES)
    drivetrain.drive_for(REVERSE, 1000, MM)
    drivetrain.turn_for(LEFT, 22, DEGREES)
    drivetrain.drive_for(REVERSE, 150, MM,wait=False)
    Intake.spin_for(REVERSE, 350, DEGREES)












  
def user_control():
    brain.screen.clear_screen()
    Intake.set_velocity(1000000, PERCENT)
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(50, PERCENT)


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
>>>>>>> Stashed changes
