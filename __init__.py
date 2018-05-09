#! python3

import sys
import re
import warnings as warner

# TODO Modularity for fun?

# TODO the entire program


class Robot:
    def __init__(self):
        self.place = {"X": 20, "Y": 20}  # X,Y space 20 per 20
        self.robot_place = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}
        self.movement = None

    def __str__(self):
        return "This robot follow the command by using the follow keywords\n" \
               "{}, {}, {}, {}, those can be followed by numbers to multiple".format(*list(self.robot_place.keys())) + \
               "\nFinally SHOW and OVER. SHOW, shows the robot place and OVER finish the program"

    def robot_movement(self, movement=None):

        if movement:

            if movement.upper() == "OVER":
                sys.exit(1)
            elif movement.upper() == "SHOW":
                return self.robot_place # TODO Proper print something
            elif movement.upper() == "HELP":
                return self

            else:

                movement = movement.split()
                movement = [i.upper() for i in movement]

                for i, k in enumerate(movement):

                    if k not in self.robot_place.keys() and not k.isdigit() and k != "SHOW" and k != "OVER":
                        warner.warn("Value not in the dictionary, deleting it. VALUE:{}".format(k))
                        del movement[i]
                    else:
                        continue

                self.movement = " ".join(movement)

                for i in ["'", "[", "]"]:
                    if i in self.movement:
                        self.movement = self.movement.replace(i, "")
                self._robot_translate()
                self._robot_move()

        else:
            warner.warn("The variable movement is not defined")

    def _robot_place(self):
        pass

    def _robot_translate(self):
        # The following code verify for the correct pattern and ignore some commands that were given wrong
        # or out of the order
        # TODO Dynamic way to identify the code pattern, basically better way

        robotic_finder = re.compile(r"({}|{}|{}|{}) ?([1-9]*)? ?(SHOW|OVER)?".format(*self.robot_place.keys())) # FIXME

        self.movement: str = robotic_finder.findall(self.movement)  # findall method shows all groups

    def _robot_move(self):
        for _, typo in enumerate(self.movement):  # reason for _, Id of the value not necessary
            print(typo)  # FIXME Coding running but not doing exactly what I want
            if typo[1] and typo[2] == "SHOW":  # Numbers of times and command
                self.robot_place[typo[0]] += int(typo[1])
                print("GOT HERE")
                return print(self.robot_place[typo[0]])
                pass  # TODO
            elif typo[1] and typo[2] == "OVER":
                self.robot_place[typo[0]] += int(typo[1])
                sys.exit(1)
            else:
                self.robot_place[typo[0]] += 1

    def _robot_process(self):
        pass

    # ANOTHER WAY ((DOWN |UP )[1-9]* ?(SHOW|OVER)?) Basically a tip


def main():
    pass


robot = Robot()
robot.robot_movement("UP 14 AFK and down down show")


if __name__ == "__main__":
    main()
