#! python3

# Stupid Robot - This program is useless, basically it's a robot that goes into places of the memory. Kinda deep....

# Made by ThinkAboutMin, a horrible programmer
# and
# Made with Pycharm to skip some silly things


# Advise: This program uses a lot of things considered poor. Please understand that I never worked with
# programs in the way I did with this one, and that I'm really dumb.
# Feel free to yell mentally on how X thing is done in such way.

# ----------------------------------------- IMPORTS -----------------------------------------

import sys
import re
import warnings as warner

# ------------------------------------------ CLASS -------------------------------------------


class Robot:
    def __init__(self):
        # Declare everything in the __init__ method, even if it's not used now, PEP8 strictly?

        self.place = (20, 20)  # X and Y
        self.robot_place = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}  # NEITHER HERE!!!
        self.movement = None
        self.robot_axis = None

    def __str__(self):
        # Here comes the nightmare return

        return"This robot follow the command by using the follow keywords\n" \
              "{}, {}, {}, {}, those can be followed by numbers to multiple".format(*list(self.robot_place.keys())) + \
              "\nFinally SHOW and OVER. SHOW, shows the robot place and OVER finish the program"

    def robot_movement(self, movement=None):

        if movement:  # No need to compare to True or False, python does it automatically if "" == FALSE and " " == TRUE
            if movement.upper() == "HELP":
                # Return the __str__ method, as it is returning itself(instance)
                print(self)
            else:
                # Check the string movement for misleading command or anything else that the robot don't accept
                movement = movement.split()
                movement = [i.upper() for i in movement]  # Make the entire string in upper case

                for i, k in enumerate(movement):
                    # FIXME Numbers pass through this code and doesn't show an warner
                    # This might not be fixed as I would need to change too many things for such...

                    if k not in self.robot_place.keys() and not k.isdigit() and k != "SHOW" and k != "OVER":
                        warner.warn("Value not in the dictionary, deleting it. VALUE:{}".format(k))  # Kinda useless
                        del movement[i]
                    else:
                        continue

                self.movement = " ".join(movement)

                for i in ["'", "[", "]"]:  # For some reason python maintain those characters after converting so...
                    if i in self.movement:
                        self.movement = self.movement.replace(i, "")  # I replace them with nothing

                self._robot_translate()
                self._robot_move()

        else:
            warner.warn("The variable movement is not defined")  # Another useless warn... Warned you!
            print(self)

    def _robot_place(self):
        self._robot_process()

        self.robot_axis = (self.robot_place["DOWN"] - self.robot_place["UP"],
                           self.robot_place["LEFT"] - self.robot_place["RIGHT"])

        placebo = ["A" for _ in range(self.place[1])]

        for i in range(0, self.place[1]):
            if i == self.robot_axis[0]:
                placebo[self.robot_axis[1]] = "#"
                print("".join(placebo))
                placebo[self.robot_axis[1]] = "A"  # Stupid way of recovering the value
            else:
                print("".join(placebo))

    def _robot_translate(self):

        # The following code verify for the correct pattern and ignore some commands that were given wrong
        # or out of the order

        robotic_finder = re.compile(r"(SHOW|OVER|{}|{}|{}|{})\s?(\d*)\s?(SHOW|OVER)?"
                                    .format(*self.robot_place.keys()))

        self.movement: str = robotic_finder.findall(self.movement)  # findall method shows all groups

    def _robot_move(self):
        for _, typo in enumerate(self.movement):  # reason for _, Id of the value not necessary. GONE TO THE VOID!
            if typo[0] == "OVER":
                bye()
                sys.exit(1)
            elif typo[0] == "SHOW":
                self._robot_place()
            elif typo[1]:
                self.robot_place[typo[0]] += int(typo[1])
            elif typo[1] and typo[2] == "SHOW":
                self.robot_place[typo[0]] += int(typo[1])
                self._robot_place()
            elif typo[1] and typo[2] == "OVER":
                self.robot_place[typo[0]] += int(typo[1])
                bye()
                sys.exit(1)
            else:
                self.robot_place[typo[0]] += 1
                if typo[2] == "SHOW":
                    self._robot_place()
                elif typo[2] == "OVER":
                    bye()
                    sys.exit(1)

    def _robot_process(self):
        # Verify if the robot passes the limit of the space and returns it in a suitable one
        for i in self.robot_place.keys():
            if i == "UP" or "DOWN":
                while self.robot_place[i] > self.place[0] - 1:
                    self.robot_place[i] %= self.place[0]
            else:
                while self.robot_place[i] > self.place[1] - 1:
                    self.robot_place[i] %= self.place[1]
                    print("OI")
        if self.robot_place["UP"] > self.robot_place["DOWN"]:
            self.robot_place["UP"] = -(self.place[0] - self.robot_place["UP"])
        else:
            pass

# ----------------------------------------- FUNCTION -------------------------------------------


def main():
    robot = Robot()  # No need to declare anything in __init__, BTW this is an instance
    while True:
        input_ = input("Please, write here your code for the robot. Need any help? type help 'pun intended'")
        robot.robot_movement(input_)
        continue  # Explicitly for readability, and understand that this loop continue until the user closes it

def bye():
    print("Bye, bye. Have a nice day")
# ---------------------------------------- Trigger --------------------------------------------
# NIGHTMARE STARTS


if __name__ == "__main__":
    main()
else:
    raise Warning("Lel, caught you trying to use this as a method")  # Silly thing of mine
