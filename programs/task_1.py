#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    n = input("Введите строку:\n")
    gl = set("ауоыиэяюеё")

    counter = 0
    for i in n:
        if i in gl:
            counter += 1
    
    print(counter)