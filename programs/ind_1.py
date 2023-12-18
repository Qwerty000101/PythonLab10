#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    A = {"a", "b", "c", "e", "t"}
    B = {"b", "c", "d", "e", "m", "u"}
    C = {"b", "c", "f", "g", "h", "u"}
    D = {"a", "d", "q", "r", "v", "w"}

    X = (A.difference(B)).union(D.difference(C))
    print(f"X = {X}")

    Y = (D.difference(A)).union(C.difference(B))
    print(f"Y = {Y}")