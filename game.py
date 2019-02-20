

# = Game Singleton ============================================================

# - Dependencies ---------------------------------
# Python Modules
import threading
import array
import threading
import math
import time
from random import random
# Local Modules
from config import *
from vector3d import *
import client
from particle import Particle
from vehicle import Vehicle

# - Game access function -------------------------
game = None


def get_game(*args):
    global game
    # Generate a game if necessary
    if(game is None):
        game = Game(*args)
    # Return the game
    return game


# - Game Object ----------------------------------
class Game:
    def __init__(self, screen):
        super().__init__()
        self.time = None
        self.ship = None
        # Setup thread for game loop
        the_client = client.get_client()

        def game_loop():
            while(True):
                # Get commands from client
                client_command = the_client.key_command
                the_client.key_clear()
                # Do game logic
                self.iterate(client_command)
                # Draw Display
                the_client.display(screen)
                # Sleep
                time.sleep(TIME_GAME_TICK)

        thread_game = threading.Thread(
            target=game_loop,
            name="Game Loop",
            daemon=True)
        thread_game.start()

    def iterate(self, player_command):
        if(self.time is None):
            return
        self.time += 1
        #
        S = self.ship
        turn_rate = 100
        if(player_command == COMMAND_UP):
            S.pitch(math.pi/turn_rate)
            S.velocity = scale_vector(S.bearing, magnitude(S.velocity))
        elif(player_command == COMMAND_DOWN):
            S.pitch(-math.pi/turn_rate)
            S.velocity = scale_vector(S.bearing, magnitude(S.velocity))
        elif(player_command == COMMAND_LEFT):
            S.yaw(math.pi/turn_rate)
            S.velocity = scale_vector(S.bearing, magnitude(S.velocity))
        elif(player_command == COMMAND_RIGHT):
            S.yaw(-math.pi/turn_rate)
            S.velocity = scale_vector(S.bearing, magnitude(S.velocity))
        elif(player_command == COMMAND_ROLL_RIGHT):
            S.roll(-math.pi/turn_rate)
            S.velocity = scale_vector(S.bearing, magnitude(S.velocity))
        elif(player_command == COMMAND_ROLL_LEFT):
            S.roll(math.pi/turn_rate)
            S.velocity = scale_vector(S.bearing, magnitude(S.velocity))
        # Move all particles
        for particle in self.particles:
            particle.take_turn(self.time)

    def start(self):
        self.time = 0
        # Populate cosmos
        self.ship = Vehicle()
        self.ship.velocity = (0, 0, AU/100)#/KILO)
        self.particles = []
        for I in range(0, 5000):
            position = (
                (random()-1/2) * 40*AU,
                (random()-1/2) * 40*AU,
                (random()-1/2) * 40*AU,
            )
            new_particle = Particle(position, random()*695000*KILO)
            self.particles.append(new_particle)
        new_particle = Particle((4*GIGA, 1*GIGA, AU), random()*695000*KILO)
        self.particles.append(new_particle)
        # Create player Spaceship
        self.particles.append(self.ship)
