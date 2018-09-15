#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import traceback

from game.cursesgame import CursesGame
from game.game import TTYGame


def parse_cl_args():
    parser = argparse.ArgumentParser(description='Play Century:Spice Road')
    parser.add_argument('nplayers', type=int, help='Number of players', choices=range(1, 6))
    parser.add_argument('--nocurses', action='store_true', help="Use the CL renderer instead of curses")
    return parser.parse_args()


if __name__ == "__main__":
    # noinspection PyBroadException
    try:
        args = parse_cl_args()
        if args.nocurses:
            # Start a game with an ugly TTY interface that will render without other fancy tools
            print("Starting a %d-player TTYGame" % args.nplayers)
            TTYGame(0, args.nplayers).loop()
        else:
            # Start a game with a nice, curses UI
            print("Starting a %d-player CursesGame" % args.nplayers)
            CursesGame(0, args.nplayers).loop()
    except Exception:
        print(traceback.format_exc())
    else:
        print("Exited with no problems")
