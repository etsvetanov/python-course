class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def robot_instances():
        return Robot.__counter


if __name__ == "__main__":
    print(Robot.robot_instances())
    x = Robot()
    print(x.robot_instances())
    y = Robot()
    print(x.robot_instances())
    print(Robot.robot_instances())
