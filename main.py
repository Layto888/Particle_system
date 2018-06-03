"""
A simple 2D particle engine.
Author: Amardjia Amine
"""

from laylib.environment import *
from particle import ParticlesEngine


def main():
    # init global environment
    test = Environment(

        1080,  # width
        720,   # height
        False,  # full screen
        'Particle Demo'  # window title
    )
    start_position = (300, 500)
    test.load_complete(ParticlesEngine(start_position))
    # go play
    test.gInstance.main_loop()
    # quit
    # test.destroy()

if __name__ == "__main__":
    main()
