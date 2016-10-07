class Robot:
    counter = 0

    def __init__(self):
        Robot.counter += 1

    def robot_instances(self):
        return Robot.counter


if __name__ == "__main__":
    x = Robot()
    print(x.robot_instances())
    y = Robot()
    print(x.robot_instances())