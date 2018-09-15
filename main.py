#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import traceback

from game.cursesgame import CursesGame

if __name__ == "__main__":
    # noinspection PyBroadException
    try:
        game = CursesGame(0, 4)
        game.loop()
    except Exception:
        print(traceback.format_exc())
