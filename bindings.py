

# = Key Bindings ==============================================================
"""Default mapping of keyboard keys onto player commands."""


# - Dependencies ---------------------------------
# Python Modules
import curses
# Local Modules
from config import *


# - Bindings -------------------------------------
KEY_BINDINGS = {
    curses.KEY_UP: COMMAND_FORWARD,
    curses.KEY_DOWN: COMMAND_BACK,
    ord('w'): COMMAND_UP,
    ord('s'): COMMAND_DOWN,
    ord('d'): COMMAND_RIGHT,
    ord('a'): COMMAND_LEFT,
    ord('e'): COMMAND_ROLL_CLOCKWISE,
    ord('q'): COMMAND_ROLL_ANTICLOCK,
    ord(' '): COMMAND_STABILIZE | COMMAND_PRIMARY,
    curses.KEY_RIGHT: COMMAND_TIME_SCALE_INCREASE,
    curses.KEY_LEFT: COMMAND_TIME_SCALE_DECREASE,
}
