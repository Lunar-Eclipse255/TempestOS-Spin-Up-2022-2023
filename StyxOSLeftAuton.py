# Library imports
from vex import *


# Begin project code
# Extends pneumatic piston
Index.set(False)
Endgame.set(False)
integral=0
timeInterval=0.05
flywheelVolts=0
KP=1
KI=2
KD=0.1
target=12
previousError=0




  




def CalculateFlyWheelVolt():
if Flywheel.current(CurrentUnits.AMP) == 0:
  global FlyWheelVoltage
  FlyWheelVoltage = 0
else:
  FlyWheelVoltage = Flywheel.power(PowerUnits.WATT)/Flywheel.current(CurrentUnits.AMP)








def PIDController():
  global integral
  global timeInteval
  global previousError
  global KP
  global KI
  global KD
  global target
  global FlyWheelVoltage
  global flywheelSpin
  global output
  while True :
      while flywheelSpin==True:
          flywheelVolts=Intake.velocity(RPM)/12.5
          CalculateFlyWheelVolt()
          error = target - FlyWheelVoltage;
          integral = integral + error * timeInterval
          derivative = (error - previousError) / timeInterval
          previousError = error
          output = KP * error + (KI * integral + KD * derivative)
          #Flywheel.spin(FORWARD, abs(output), VOLT)
          #wait(timeInterval, SECONDS)
 def run_on_broadcast1():
   PIDController()






#Creates function to rectract pneumatic piston for index
def index_close_burst():
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




def index_autonomous():
   Flywheel.spin(FORWARD, 13, VOLT)
   wait(5, SECONDS)
   Index.set(True)
   wait(0.5, SECONDS)
   Index.set(False)
   wait(0.7, SECONDS)
   Index.set(True)
   wait(0.5, SECONDS)
   Index.set(False)
   wait(0.5, SECONDS)
   controller_1.screen.clear_screen()
   controller_1.screen.print("index")
   Flywheel.stop()




def index_far():
   global flywheelSpin
   flywheelSpin=True
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
   flywheellSpin=False
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


my_event = Event()
my_event(run_on_broadcast1)
wait(15, MSEC)
my_event.broadcast()


#Programs the face buttons
controller_1.buttonY.pressed(index_close_burst)
controller_1.buttonB.pressed(index_far)
controller_1.buttonLeft.pressed(endgame)
controller_1.buttonX.pressed(index_one)


#Sets the robot's different velocities
Intake.set_velocity(10000000, PERCENT)
Flywheel.set_velocity(1000000, PERCENT)
drivetrain.set_drive_velocity(75, PERCENT)
drivetrain.set_turn_velocity(50, PERCENT)


#Reverses the values of two motors






def pre_autonomous():
   Intake.set_velocity(100, PERCENT)
   drivetrain.set_drive_velocity(50, PERCENT)
   drivetrain.set_turn_velocity(10, PERCENT)
  
 
def autonomous():
   right_motor_a = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
   right_motor_b = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
   right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
   left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
   left_motor_b = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)
   drivetrain.drive_for(FORWARD, -20, MM,wait=False)
   Intake.spin_for(FORWARD, -300, DEGREES)
   drivetrain.set_drive_velocity(50, PERCENT)
   drivetrain.drive_for(FORWARD, 200, MM)
  




  


























  


def user_control():
   right_motor_a = Motor(Ports.PORT13, GearSetting.RATIO_18_1, False)
   right_motor_b = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
   right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
   left_motor_a = Motor(Ports.PORT18, GearSetting.RATIO_18_1, True)
   left_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
   left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
   Intake.set_velocity(100, PERCENT)
   drivetrain.set_drive_velocity(75, PERCENT)
   drivetrain.set_turn_velocity(10, PERCENT)




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
