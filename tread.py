#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-

import threading
from time import sleep


def loop(x):
    while True:
        print(x)
        sleep(2)


t1 = threading.Thread(target=loop, args=[1])
t2 = threading.Thread(target=loop, args=[1])

t1.start()
t2.start()
