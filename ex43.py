
# * Map
#   - next_scene
#   - opening_scene
# * Engine
#   - play
# * Scene
#   - enter
#   * Death
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Bridge
#   * Escape Pod

from sys import exit
from random import randint

class Map(object):
    """The map of all the rooms."""

    def __init__(self, start_scene):
        pass

    def next_scene(self):
        pass

    def opening_scene(self):
        pass

class Engine(object):
    """The cental loop that runs the game"""

    def __init__(self, scene_map):
        self.description = """
        Aliens have invaded a space ship
        and our hero has to go through a maze of rooms defeating them
        so he can escape into an escape pod to the planet below.
        The game will be more like a Zork or Adventure type game
        with text outputs and funny ways to die.
        The game will involve an engine that runs a map full of rooms or scenes.
        Each room will print its own description when the player enters it
        and then tell the engine what room to run next out of the map.
        """

        pass

    def play(self):
        pass

class Scene(object):
    """Parent class for individual rooms."""

    def __init__(self):
        pass

    def enter(self):
        pass

class Death(Scene):
    """This is when the player dies and should be something funny."""

    def __init__(self, why):
        self.why = why

    def enter(self):
        print "\n", self.why, "You die. Good job!"
        exit(0)

class CentralCorridor(Scene):
    """
    This is the starting point.

    It has a Gothon already standing there
    they have to defeat with a joke before continuing.
    """

    def enter(self):
        print """
        The Gothons have invaded your ship.
        You are standing in the Central Corridor.
        There is a Gothon in front of you.
        He says, 'Tell me a joke.'
        """

        joke = raw_input('> ')

        if len(joke) < 5:
            print "He says, 'That was pathetic.' "
            death = Death("He throws a giant, rotten tomato at you.")
            death.enter()
        else:
            print "He chuckles. He laughs. He chokes on his own spit and dies."
            print "Behind where he was standing, a door says 'Armory.'"
            print "You go through the door."
            return 'laser_weapon_armory'

class LaserWeaponArmory(Scene):
    """
    This is where the hero gets a neutron bomb

    Use the bomb to blow up the ship before getting to the escape pod.
    It has a keypad the hero has to guess the number for.
    """

    def enter(self):
        print "There is a neutron bomb here, locked to the wall."
        print "The sign above it says, 'Enter digit to remove.'"
        print "There is a keypad on it with the numbers 0-9."

        n = randint(0,9)
        resp = int(raw_input('> '))
        print "you type %d, the lock wanted %d" % (resp, n)
        if n == resp:
            print "You hear an audible click, and the lock opens."
            print "An alarm sounds."
            print "You take the bomb and walk to the door marked 'Bridge'"
            return 'the_bridge'
        else:
            print "The sign clears, then prints, 'Wrong-o.'"
            print "The bomb explodes."
            death = Death("The ship, the Gothons, and you are blown to pieces.")
            death.enter()

class TheBridge(Scene):
    """Another battle scene with a Gothon where the hero places the bomb."""

    def __init__(self):
            self.rock_paper_scissors = ['rock', 'paper', 'scissors']

    def enter(self):
        print "You enter the Bridge."
        print "Another Gothon has heard the alarm, and rushes into the bridge."
        print "He is heavily armed."
        print "You say, 'Rock, Paper, Scissors?'"
        print "The Gothon says, 'Sure!'"

        while True:
            raw_input('Press "enter" to play.')
            you = randint(0, 2)
            gothon = randint(0, 2)
            print "You show: ", self.rock_paper_scissors[you]
            print "He shows: ", self.rock_paper_scissors[gothon]
            if you == (gothon + 1) % 3:
                print "The Gothon loses."
                print "He shrieks and disappears in a puff of smoke."
                print "You head for the door marked 'Escape pod.'"
                return 'escape_pod'
            elif gothon == (you + 1) % 3:
                print "You lose."
                death = Death("You shriek and disappear in a puff of smoke.")
                death.enter()
            else:
                print "Rats. Go again."

class EscapePod(Scene):
    """Where the hero escapes but only after guessing the right escape pod."""

    def enter(self):
        print "You enter the room and see two escape pods."
        print "A sign overhead flashes, 'Escape pod needs refueling.'"
        print ("The lights for the arrows underneath, "
                "to show which pod needs fuel, "
                "are burnt out.")
        print "The five minute warning for the bomb begins beeping."
        while True:
            pod = raw_input("Do you choose the right pod or the left? ")
            if pod == 'right' or pod == 'left':
                break
            else:
                print "Please type 'right' or 'left.' Time is short."

        action = "You guess, jump into the %s pod, " % pod
        action += "and press the button marked 'Go.'"
        print action
        print "The pod launches, you rush into space."

        if randint(0, 1) == 0:
            print "You speed away. Five minutes later, the bomb explodes."
            print "The spaceship and Gothons are destroyed."
            print "You head to the planet below."
            return 'you_win'
        else:
            print "The pod sputters to a halt, feet outside the exit."
            print "No fuel. No way back."
            death = Death("Four-and-a-half minutes later, the bomb explodes.")
            death.enter()

a_map = Map('central_corridor')
a_game = Engine(a_map)

a_game.play()
