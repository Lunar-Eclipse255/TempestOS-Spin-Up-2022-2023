#Left Autonomous
def autonomous_1 ():
   drivetrain.drive_for(REVERSE, 50, MM)
   indexCloseBurst()
   wait(1, SECONDS)
   drivetrain.drive_for(FORWARD, 50, MM)
   drivetrain.turn_for(RIGHT, 50, DEGREES)
   drivetrain.drive_for(FORWARD, 1500, MM)
   drivetrain.turn_for(LEFT, 87, DEGREES)
   Flywheel.spin(FORWARD)
   intakeCloseBurst()
