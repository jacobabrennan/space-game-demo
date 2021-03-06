# Space Game Demo

A real 3D environment for the Terminal. This is a simulation of a spaceship within the inner solar system. Point yourself anywhere and fly there with full three dimensional control. Distances and sizes used throughout the project are real measurements of the cosmos, with the total distance between game objects of 200 million light years. Gravity is implemented but, sadly, crashing into planets isn't finished yet.

## Getting Started

To get started, clone or download the repo. Then open your terminal and navigate to the project directory. Execute the file "main.py" using Python, and the game will start.

```
$ cd space-game-demo
$ py main.py
```

### Prerequisites

You must have Python version 3 install and configured properly for your system.

If you are running the game on Windows, you must also install the windows-curses library. The library can be installed via Pip using the following command:

```
python -m pip install windows-curses
```

### Controls

Control your spaceship with the keyboard, using these keys:
* W+S: Pitch control (vertical view angle)
* A+D: Yaw control (horizontal view angle)
* Q+E: Roll control (rotates view screen)
* Arrow Up + Down: Increase thrust, Decrease thrust
* Arrow Right + Left: Increase / Decrease time scale
* Spacebar: Stabilize rotation and Decelerate
