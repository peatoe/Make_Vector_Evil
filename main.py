import anki_vector
import random

random_number = random.randint(1, 2)

# Create the robot connection
with anki_vector.Robot() as robot:
    # Run your commands
    if random_number == 1:
        robot.behavior.drive_on_charger()
        robot.behavior.say_text("I can finaly sleep and escape this nightmare that is my life!")
    else:
        robot.behavior.find_faces()
        robot.behavior.say_text("God, you are so ugly!")
