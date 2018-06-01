"""
A simple 2D particle engine.
Author: Amardjia Amine
"""

from laylib.environment import *
from particle import ParticlesEngine

# res = Resources('data')
# res.save_res_info(data, 'resources.dat', False)
# res.save_res_info(levels, 'levels.dat', True)


def main():
    # init global environment
    test = Environment(

        1080,  # width
        720,   # height
        False,  # full screen
        'Particle Demo'  # window title
    )
    p = (300, 500)

    test.load_complete(ParticlesEngine(p))

    # go play
    test.gInstance.main_loop()
    # quit
    # test.destroy()


if __name__ == "__main__":
    main()
