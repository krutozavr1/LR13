#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def average_geom(*args):
    """finds average geom number if args are provided"""
    if args:
        values = [float(arg) for arg in args]
        values.sort()
        n = len(values)
        av_geom = math.prod(values) ** (1 / n)
        print(f"av geom is {av_geom}")
    else:
        print("No arguments")


if __name__ == "__main__":
    average_geom(1, 5, 20, 100)
