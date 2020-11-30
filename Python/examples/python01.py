#!/usr/bin/env python3

# Receiving 2 arguments and adding both.

import sys

numargs = len(sys.argv)

if numargs < 3:
    print("Você deve inserir até 2 argumentos...")
    exit(1)
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a+b
    print(f"A soma de {a} e {b} é {c}")
