# Maze Solver

- GUI desktop app that automatically renders a random maze and solves it using a recursive Python algorithm.
- The GUI is made with tkinter Python native library.

## Lauching the maze

Clone the repo and execute the main.py file.

## Algorithm

The maze solver is created using Oriented Object Programming and recursivity : 
- The maze is a bidimensional matrix of Cells, drawn on the screen with the help of Points and Lines objects
- The maze is solved recursively with a depth-first algorithm

## A note on Tkinter

Tkinter is a standard GUI library of Python and does not need any package installation.

HOWEVER for GNU/Linux users, tkinter is NOT included in the native Python3 installed.
> You need to install python3-tk with you Linux distro prefered package manager (on Ubuntu: apt) to be able to launch the app

