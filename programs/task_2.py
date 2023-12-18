#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    n_first = set(input("Введите первую строку:\n"))
    n_second = set(input("Введите вторую строку:\n"))
    symbols = n_first.intersection(n_second)

    print("Общие символы: ")
    for i in symbols:
        print(i,end=" ")