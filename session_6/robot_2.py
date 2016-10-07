class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def robot_instances():
        return Robot.__counter


a = Robot()

print(Robot.robot_instances())

print(a.robot_instances())