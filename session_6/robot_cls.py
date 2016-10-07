class Robot:
    __counter = 0

    def __init__(self):
        Robot.__counter += 1

    @classmethod
    def robot_instances(cls):
        return cls.__counter


if __name__ == "__main__":
    print(Robot.robot_instances())
    x = Robot()
    print(x.robot_instances())
    y = Robot()
    print(x.robot_instances())
    print(Robot.robot_instances())

