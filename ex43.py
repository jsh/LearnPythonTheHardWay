
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
    """docstring for Map."""
    def __init__(self, start_scene):
        pass

    def next_scene(self):
        pass

    def opening_scene(self):
        pass

class Engine(object):
    """docstring for Engine."""
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Scene(object):
    """docstring for Scene."""
    def __init__(self):
        pass

    def enter(self):
        pass

class Death(Scene):
    """docstring for Death."""
    def enter(self):
        pass

class CentralCorridor(Scene):
    """docstring for CentralCorridor"""
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    """docstring for LaserWeaponArmory"""
    def enter(self):
        pass

class TheBridge(Scene):
    """docstring for Bridge"""
    def enter(self):
        pass

class EscapePod(Scene):
    """docstring for EscapePod"""
    def enter(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)

a_game.play()
