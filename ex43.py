
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
        description = """
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

    def enter(self):
        pass

class CentralCorridor(Scene):
    """
    This is the starting point.

    It has a Gothon already standing there
    they have to defeat with a joke before continuing.
    """

    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    """
    This is where the hero gets a neutron bomb

    Use the bomb to blow up the ship before getting to the escape pod.
    It has a keypad the hero has to guess the number for.
    """

    def enter(self):
        pass

class TheBridge(Scene):
    """Another battle scene with a Gothon where the hero places the bomb."""

    def enter(self):
        pass

class EscapePod(Scene):
    """Where the hero escapes but only after guessing the right escape pod."""

    def enter(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)

a_game.play()
