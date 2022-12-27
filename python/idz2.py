#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def average_harmon(*args):
    """ finds average harmonic number if args are provided"""
    if args:
        values = [float(arg) for arg in args]
        values.sort()
        n = len(values)
        sum = 0
        for val in values:
            sum += 1/ val
        sr_harm = n / sum
        print(sr_harm)
    else:
        print("No arguments")


if __name__ == "__main__":
    average_harmon(10, 15, 6, 3)
