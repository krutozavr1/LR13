#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сумму модулей аргументов, расположенных после минимального по модулю аргумента."""

def modul_sum(*args):
    """finds summ of moduls after min number """
    if args:
        values = [abs(float(arg)) for arg in args[0]]
        summa = sum(values[values.index(min(values)) + 1 : ])

        print(f"sum is {summa}")
    else:
        print("No arguments")


if __name__ == "__main__":
    str = input()
    modul_sum(str.split(' '))
